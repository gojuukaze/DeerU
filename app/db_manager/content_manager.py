from app.app_models.content_model import Article, Category, ArticleCategory, Tag, ArticleTag, ArticleMeta, Comment, \
    FlatPage


################## Article ###############
def create_article(title, content):
    Article.objects.create(title=title, content=content)


def get_article_by_id(id):
    try:
        return Article.objects.get(id=id)
    except:
        return None


def get_last_article_by_id(id):
    try:
        return Article.objects.filter(id__lt=id).order_by('-id')[0]
    except:
        return None


def get_next_article_by_id(id):
    try:
        return Article.objects.filter(gt__lt=id).order_by('-id')[0]
    except:
        return None


def get_article_by_title(title):
    try:
        return Article.objects.get(title=title)
    except:
        return None


def filter_article_order_by_id(desc=True):
    return Article.objects.filter().order_by('-id' if desc else 'id')


def get_all_article():
    return Article.objects.all()


def filter_article_by_id():
    return Article.objects.filter(id=id)


def filter_article_by_category(category_id):
    article_ids = list(filter_article_category_by_category(category_id).values_list('article_id', flat=True))
    if article_ids:
        return Article.objects.filter(id__in=article_ids)
    else:
        return Article.objects.none()


def filter_article_by_tag(tag_id):
    article_ids = list(filter_article_tag_by_tag(tag_id).values_list('article_id', flat=True))
    if article_ids:
        return Article.objects.filter(id__in=article_ids)
    else:
        return Article.objects.none()


################### ArticleMeta ###################
def get_or_create_article_meta(id):
    return ArticleMeta.objects.get_or_create(article_id=id)


def get_article_meta_by_article(id):
    try:
        return ArticleMeta.objects.get(article_id=id)
    except:
        return None


############# Category ######################

def get_all_category():
    return Category.objects.all()


def filter_category_by_article(a_id):
    c_ids = list(filter_article_category_by_article(a_id).values_list('category_id', flat=True))
    if c_ids:
        return Category.objects.filter(id__in=c_ids)
    else:
        return Category.objects.none()


def get_category_by_id(id):
    try:
        return Category.objects.get(id=id)
    except:
        return None


def filter_category_by_start_name(name):
    return Category.objects.filter(name__istartswith=name)


##################### ArticleCategory ##########################

def filter_article_category_by_article(a_id):
    return ArticleCategory.objects.filter(article_id=a_id)


def filter_article_category_by_category(c_id):
    return ArticleCategory.objects.filter(category_id=c_id)


def get_or_create_article_category(a_id, c_id):
    return ArticleCategory.objects.get_or_create(article_id=a_id, category_id=c_id)


############# Tag ######################

def get_all_tag():
    return Tag.objects.all()


def get_tag_by_id(id):
    try:
        return Tag.objects.get(id=id)
    except:
        return None


def filter_tag_by_start_name(name):
    return Tag.objects.filter(name__istartswith=name)


def create_tag(name):
    return Tag.objects.create(name=name)


def get_or_create_tag(name):
    return Tag.objects.get_or_create(name=name)


def filter_tag_by_name_list(name):
    return Tag.objects.filter(name__in=name)


def filter_tag_by_article(a_id):
    t_ids = list(filter_article_tag_by_article(a_id).values_list('tag_id', flat=True))
    if t_ids:
        return Tag.objects.filter(id__in=t_ids)
    else:
        return Tag.objects.none()


############# ArticleTag ######################

def filter_article_tag_by_article(a_id):
    return ArticleTag.objects.filter(article_id=a_id)


def filter_article_tag_by_tag(t_id):
    return ArticleTag.objects.filter(tag_id=t_id)


def get_or_create_article_tag(a_id, t_id):
    return ArticleTag.objects.get_or_create(article_id=a_id, tag_id=t_id)


#################  Comment  #######################

def create_comment(nickname, email, content, article_id, root_id, to_id, type):
    return Comment.objects.create(nickname=nickname, email=email, content=content, article_id=article_id,
                                  root_id=root_id, to_id=to_id, type=type)


def filter_comment_by_article(a_id):
    return Comment.objects.filter(article_id=a_id)


#################  FlatPage  #######################

def create_flatpage(title, content):
    return FlatPage.objects.create(title=title, content=content)


def get_flatpage_by_id(id):
    try:
        return FlatPage.objects.get(id=id)
    except:
        return None


def get_flatpage_by_url(url):
    try:
        FlatPage.objects.get(url=url)
    except:
        return None


def all_flatpage():
    return FlatPage.objects.all()
