import sys
from pprint import pprint

from django.core.management import BaseCommand
from django.core.management.base import OutputWrapper

from app.app_models.content_model import Article, Category, Tag, ArticleMeta, ArticleCategory, ArticleTag, Comment
from app.manager.ct_manager import update_one_to_many_relation_model
from tool.datetime_helper import str_to_datetime

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


class Command(BaseCommand):
    """
    从wordpress xml文件导入

    1.评论暂不支持审核，所有不会导入未审核的评论，如果需要去掉get_comment()中对应的部分

    2.日期格式必须为： 2018-05-02 15:23:22

    3.对评论的回复会自动在内容前添加 "回复 xx："，如果不需要去掉save_comment()中对应部分

    4.不会导入草稿

    python manage.py import_wordpress

    """

    def add_arguments(self, parser):
        parser.description = '''从wordpress xml文件导入
    1.评论暂不支持审核，所以不会导入未审核的评论
    2.日期格式必须为： 2018-05-02 15:23:22'''

        parser.add_argument('xml_path', type=str)

        parser.add_argument(
            '--mode',
            default='a',
            choices=['a', 'c', 't'],
            dest='mode',
            help='default:a; 想要导入的内容 ( a:article+comment+category+tag, c:category, t:tag )',
        )
        parser.add_argument(
            '--nwp',
            default='{http://wordpress.org/export/1.2/}',
            dest='nwp',
            help='xml namespace: wp; xml文件中命名空间wp的内容',
        )
        parser.add_argument(
            '--ncontent',
            default='{http://purl.org/rss/1.0/modules/content/}',
            dest='ncontent',
            help='xml namespace: content; xml文件中命名空间content的内容',
        )
        parser.add_argument(
            '--cover',
            choices=['y', 'n', 'ask'],
            default='ask',
            help='Do you want to used xml data cover database data；是否用xml文件的内容覆盖数据库中的相同内容；（y: cover; n: donot cover; ask:ask me）',
        )

    def is_cover(self, text):

        if self.cover == 'ask':
            while True:
                self.info(text + ' ( y:是，覆盖; n:不，跳过这项; ay:总是，不再询问; an:总不，不再询问 ):')
                s = input()
                if s not in ['y', 'n', 'ay', 'an']:
                    self.error("无效输入：%s'" % s)
                else:
                    break
            if s == 'y':
                return True
            elif s == 'n':
                return False
            elif s == 'ay':
                self.cover = 'y'
            elif s == 'an':
                self.cover = 'n'

        if self.cover == 'y':
            return True
        elif self.cover == 'n':
            return False

    def get_category(self):
        for node in self.root.findall(self.nwp + 'category'):
            key = node.find(self.nwp + 'category_nicename').text
            name = node.find(self.nwp + 'cat_name').text
            parent = node.find(self.nwp + 'category_parent').text
            self.category[key] = {'name': name, 'parent': parent}

    def save_category(self):
        names = [c['name'] for key, c in self.category.items()]
        if len(set(names)) != len(names):
            self.error('导入分类失败，存在相同名称的分类')
            return
        for key, c in self.category.items():
            if c['parent']:
                continue
            try:
                old_c = Category.objects.get(name=c['name'])
                if self.is_cover('已存在相同分类(%s),是否覆盖已有数据？' % (old_c.name)):
                    old_c.father_id = -1
                    old_c.save()
                new_c = old_c
            except:
                new_c = Category.objects.create(name=c['name'])
            new_c.m_order = new_c.id

            new_c.save()

            c['id'] = new_c.id

        for key, c in self.category.items():
            if not c['parent']:
                continue
            father_key = c['parent']
            father_id = self.category[father_key]['id']
            try:
                old_c = Category.objects.get(name=c['name'])
                if self.is_cover('已存在相同分类(%s),是否覆盖已有数据？' % old_c.name):
                    old_c.father_id = father_id
                    old_c.save()

                new_c = old_c
            except:
                new_c = Category.objects.create(name=c['name'], father_id=father_id)
            new_c.m_order = new_c.id

            new_c.save()
            c['id'] = new_c.id

    def get_tag(self):
        for node in self.root.findall(self.nwp + 'tag'):
            key = node.find(self.nwp + 'tag_slug').text
            name = node.find(self.nwp + 'tag_name').text
            self.tag[key] = {'name': name}

    def save_tag(self):
        for key, t in self.tag.items():
            new_tag, is_create = Tag.objects.get_or_create(name=t['name'])
            t['id'] = new_tag.id

    def get_article(self):
        for node in self.root.findall('item'):
            type = node.find(self.nwp + 'post_type').text
            if type != 'post':
                continue

            status = node.find(self.nwp + 'status').text
            if status == 'draft':
                continue

            title = node.find('title').text
            post_date = str_to_datetime(node.find(self.nwp + 'post_date').text)
            content = node.find(self.ncontent + 'encoded').text or ''
            c = []
            t = []
            for temp in node.findall('category'):
                if temp.attrib['domain'] == 'category':
                    c.append(temp.attrib['nicename'])
                else:
                    t.append(temp.attrib['nicename'])
            read_num = 0
            for temp in node.findall(self.nwp + 'postmeta'):
                flag = False
                for temp2 in temp:
                    if temp2.text == 'post_views_count':
                        flag = True
                        continue
                    if flag:
                        read_num = temp2.text
                        break
                if flag:
                    break

            self.article.append({'title': title, 'created_time': post_date, 'read_num': read_num,
                                 'category': c, 'tag': t, 'content': content})

    def save_article(self):
        for a in self.article:
            new_a_meta = None
            try:
                old_a = Article.objects.get(title=a['title'])
                if self.is_cover('存在相同标题的文章（%s）,是否覆盖已有数据？' % old_a.title):
                    old_a.content = a['content']
                    old_a.created_time = a['created_time']
                    old_a.save()
                    new_a = old_a
                    new_a_meta = ArticleMeta.objects.get(article_id=new_a.id)
                    new_a_meta.read_num = 0
                    new_a_meta.comment_num = 0
                    new_a_meta.save()
                new_a = old_a
            except:
                new_a = Article.objects.create(title=a['title'], content=a['content'], created_time=a['created_time'])
                new_a_meta = ArticleMeta.objects.get(article_id=new_a.id)
            if new_a_meta:
                new_a_meta.read_num = a['read_num']
                new_a_meta.save()
            a['id'] = new_a.id

    def save_article_category(self):

        for a in self.article:
            id = a.get('id')
            if not id:
                continue
            c_ids = []
            for c in a['category']:
                c_id = self.category[c].get('id')
                if c_id:
                    c_ids.append(int(c_id))

            update_one_to_many_relation_model(ArticleCategory, 'article_id', id, 'category_id', c_ids,
                                              lambda x: x, old_many_ids=None)

    def save_article_tag(self):

        for a in self.article:
            id = a.get('id')
            if not id:
                continue
            t_ids = []
            for t in a['tag']:
                t_ids.append(int(self.tag[t].get('id')))

            update_one_to_many_relation_model(ArticleTag, 'article_id', id, 'tag_id', t_ids,
                                              lambda x: x, old_many_ids=None)

    def get_comment(self):
        pos = 0
        for node in self.root.findall('item'):

            type = node.find(self.nwp + 'post_type').text
            if type != 'post':
                continue
            status = node.find(self.nwp + 'status').text
            if status == 'draft':
                continue

            article_id = self.article[pos].get('id')
            pos += 1
            if not article_id:
                continue
            comments = node.findall(self.nwp + 'comment')
            if not comments:
                continue
            temp_comment = {}
            for cm in comments:
                wp_id = cm.find(self.nwp + 'comment_id').text

                nickname = cm.find(self.nwp + 'comment_author').text
                email = cm.find(self.nwp + 'comment_author_email').text
                created_time = cm.find(self.nwp + 'comment_date').text
                content = cm.find(self.nwp + 'comment_content').text

                # 不导入未审核的
                status = cm.find(self.nwp + 'comment_approved').text
                if not status:
                    continue

                parent = cm.find(self.nwp + 'comment_parent').text
                temp_comment[wp_id] = {'nickname': nickname, 'email': email, 'created_time': created_time,
                                       'content': content, 'status': status, 'parent': parent}
            self.comment[article_id] = temp_comment

    def save_comment(self):
        """
        这里假定了评论一定是按添加顺序读取的(时间升序)，如果出现bug，需要先按时间或者id排序
        :return:
        """
        for a_id, a_cm in self.comment.items():
            if not a_cm:
                continue
            # wp评论id对应的新comment id
            wpid_to_commentid = {}
            wpid_to_nickname = {}
            # wp评论id对应评论的root id
            wpid_to_comment_rootid = {}
            for wp_id, cm in a_cm.items():

                wpid_to_nickname[wp_id] = cm['nickname']

                parent = cm['parent']
                if int(parent) == 0:
                    root_id = -1
                    to_id = -1
                    type = 201
                else:
                    type = 202
                    root_id = wpid_to_comment_rootid[parent]
                    to_id = wpid_to_commentid[parent]

                    # content前添加 回复xxx

                    cm['content'] = '<p>回复 <span style="color: rgb(44, 130, 201);">' + wpid_to_nickname[
                        parent] + ' </span>:</p>' + cm['content']

                new_cm = Comment.objects.create(nickname=cm['nickname'], content=cm['content'],
                                                created_time=cm['created_time'], type=type,
                                                email=cm['email'], article_id=a_id, root_id=root_id, to_id=to_id)
                wpid_to_commentid[wp_id] = new_cm.id
                if int(parent) == 0:
                    wpid_to_comment_rootid[wp_id] = new_cm.id
                else:
                    wpid_to_comment_rootid[wp_id] = root_id

    def handle(self, *args, **options):
        self.error = self.stderr.write

        info_out = OutputWrapper(sys.stdout)
        info_out.style_func = self.style.WARNING
        self.info = info_out.write

        success_out = OutputWrapper(sys.stdout)
        success_out.style_func = self.style.SUCCESS
        self.success = success_out.write

        self.nwp = options['nwp']
        self.ncontent = options['ncontent']
        self.cover = options['cover']
        mode = options['mode']

        with open(options['xml_path'])as f:
            s = f.read()
        self.root = ET.fromstring(s)[0]

        self.category = {}

        self.tag = {}

        self.article = []
        self.comment = {}

        if 'c' in mode or 'a' in mode:
            self.info('导入分类中...')

            self.get_category()
            self.save_category()

            self.success('导入分类完成')

        if 't' in mode or 'a' in mode:
            self.info('导入标签中...')

            self.get_tag()
            self.save_tag()

            self.success('导入标签完成')

        if 'a' in mode:
            self.info('导入文章中...')
            self.get_article()
            self.article.sort(key=lambda x: x['created_time'])
            self.save_article()
            self.success('导入文章完成')

            self.info('导入文章分类中...')
            self.save_article_category()
            self.success('导入文章分类完成')

            self.info('导入文章标签中...')
            self.save_article_tag()
            self.success('导入文章标签完成')

            self.info('导入评论中...')
            self.get_comment()
            self.save_comment()
            self.success('导入评论完成')
