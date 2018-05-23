import re

from tool.kblog_exceptions import ExpressionTypeError
from tool.kblog_html import Tag


class BaseExpression(object):
    result = None

    def __init__(self, args):
        """
        如：fa | xxx
        xxx是args
        :param args:
        """
        self.args = args
        self.result = None

    def calculate(self):
        """
        获取结果，要重写
        :return:
        """
        pass

    def get_result(self):
        """
        返回表达式的处理结果，类型不固定
        :return:
        """
        if not self.result:
            self.calculate()
        return self.result

    def __str__(self):
        return '<%s>:"%s"'%(self.__class__,self.args)


class Img(BaseExpression):
    """
    img表达式

    {% img|id_or_name %}     --> 匹配顺序 id>name

    {% img|id= 1 %}          --> 匹配 id

    {% img|name= xx %}          --> 匹配 name.startswith('xx')

    {% img|id=xx | style= xx %}

    返回tag
    """

    def calculate(self):
        from app.db_manager.other_manager import get_image_by_id, filter_image_by_start_name
        if not self.args:
            self.args = ''
        self.args = self.args.strip()

        temp_args = self.args.split('|')
        img = None
        id_or_name = temp_args[0].strip()
        if re.search(r'=', id_or_name):
            k, v = id_or_name.split('=')
            k = k.strip()
            v = v.strip()
            if k == 'id':
                img = get_image_by_id(v)
            elif k == 'name':
                try:
                    img = filter_image_by_start_name(v)[0]
                except:
                    img = None
        else:
            img = get_image_by_id(id_or_name)
            if not img:
                try:
                    img = filter_image_by_start_name(id_or_name)[0]
                except:
                    img = None

        img_tag = Tag('img')
        if img:
            img_tag.set_attr('src', img.img.url)
        for attr in temp_args[1:]:
            k, v = attr.split('=')
            img_tag.set_attr(k, v)
        self.result = img_tag


class Fa(BaseExpression):
    """
    fontawesome图标表达式

    {% fa|fas xx %}
    {% fa|svg= fas xx|style=  color:xx; %}

    返回tag
    """

    def calculate(self):
        if not self.args:
            self.args = ''
        self.args = self.args.strip()
        attrs = {'class': 'icon'}
        svg = ''
        if re.search(r'\|', self.args):
            for k, v in [temp.split('=') for temp in self.args.split('|')]:
                k = k.strip()
                v = v.strip()
                if k == 'svg':
                    svg = v
                elif k == 'style':
                    attrs['style'] = v
        else:
            svg = self.args
        span = Tag('span', attrs=attrs)
        span.append(Tag('i', attrs={'class': svg}))
        self.result = span


class Cat(BaseExpression):
    """
    分类表达式
    {% cat| 值 | 返回值(name/url) %}

    {% cat| xx | name %} --> 匹配：id=xx 或 name.startswith(xx) 返回name
    {% cat| name = xx | name %} --> 匹配name.startswith(xx) 返回name
    {% cat| id = xx | url %} --> 匹配id=xx 返回url

    """

    def calculate(self):
        from app.db_manager.content_manager import get_category_by_id, filter_category_by_start_name
        if not self.args:
            self.args = ''
        self.args = self.args.strip()

        if re.search(r'\|', self.args):
            temp_args = self.args.split('|')
            temp_args[-1] = temp_args[-1].strip()
            if temp_args[-1] not in ['name', 'url']:
                raise ExpressionTypeError('表达式 cat 最后一个参数仅支持 "name","url"')
            category = None
            if re.search(r'=', temp_args[0]):
                k, v = temp_args[0].split('=')
                k = k.strip()
                v = v.strip()
                if k == 'id':
                    category = get_category_by_id(v)
                elif k == 'name':
                    category = filter_category_by_start_name(v)[0]
            else:
                v = temp_args[0].strip()
                category = get_category_by_id(v)
                if not category:
                    category = filter_category_by_start_name(v)[0]
        else:
            raise ExpressionTypeError('表达式 cat 至少需要一个参数')

        if not category:
            self.result = ''

        if temp_args[-1] == 'name':
            self.result = category.name
        elif temp_args[-1] == 'url':
            pass
