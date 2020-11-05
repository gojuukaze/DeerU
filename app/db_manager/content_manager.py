from app.app_models.content_model import Article, Category, ArticleCategory, Tag, ArticleTag, ArticleMeta, Comment, \
    FlatPage

################## Article ###############
from app.consts import CommentStatusChoices


def create_article(title, content):
    """
    Create an article.

    Args:
        title: (str): write your description
        content: (str): write your description
    """
    Article.objects.create(title=title, content=content)


def get_article_by_id(id):
    """
    Get an article by id.

    Args:
        id: (str): write your description
    """
    try:
        return Article.objects.get(id=id)
    except:
        return None


def get_last_article_by_id(id):
    """
    Get the last article with the given id.

    Args:
        id: (int): write your description
    """
    try:
        return Article.objects.filter(id__lt=id).order_by('-id')[0]
    except:
        return None


def get_next_article_by_id(id):
    """
    Return the next article by id

    Args:
        id: (int): write your description
    """
    try:
        return Article.objects.filter(gt__lt=id).order_by('-id')[0]
    except:
        return None


def get_article_by_title(title):
    """
    Get an article by title

    Args:
        title: (str): write your description
    """
    try:
        return Article.objects.get(title=title)
    except:
        return None


def filter_article_order_by_id(desc=True):
    """
    Returns an article by article id.

    Args:
        desc: (str): write your description
    """
    return Article.objects.filter().order_by('-id' if desc else 'id')


def all_article():
    """
    Return all article objects.

    Args:
    """
    return Article.objects.all()


def filter_article_by_id():
    """
    Filter article by id

    Args:
    """
    return Article.objects.filter(id=id)


def filter_article_by_category(category_id):
    """
    Filter article by article id

    Args:
        category_id: (int): write your description
    """
    article_ids = list(filter_article_category_by_category(category_id).values_list('article_id', flat=True))
    if article_ids:
        return Article.objects.filter(id__in=article_ids)
    else:
        return Article.objects.none()


def filter_article_by_tag(tag_id):
    """
    Filter article by article_id

    Args:
        tag_id: (str): write your description
    """
    article_ids = list(filter_article_tag_by_tag(tag_id).values_list('article_id', flat=True))
    if article_ids:
        return Article.objects.filter(id__in=article_ids)
    else:
        return Article.objects.none()


################### ArticleMeta ###################
def get_or_create_article_meta(id):
    """
    Get an article meta data.

    Args:
        id: (str): write your description
    """
    return ArticleMeta.objects.get_or_create(article_id=id)


def get_article_meta_by_article(id):
    """
    Returns the meta - id

    Args:
        id: (todo): write your description
    """
    try:
        return ArticleMeta.objects.get(article_id=id)
    except:
        return None


############# Category ######################

def get_all_category():
    """
    Return all category objects.

    Args:
    """
    return Category.objects.all()


def filter_category_by_article(a_id):
    """
    Filter article by article

    Args:
        a_id: (str): write your description
    """
    c_ids = list(filter_article_category_by_article(a_id).values_list('category_id', flat=True))
    if c_ids:
        return Category.objects.filter(id__in=c_ids)
    else:
        return Category.objects.none()


def get_category_by_id(id):
    """
    Get a category by its id.

    Args:
        id: (int): write your description
    """
    try:
        return Category.objects.get(id=id)
    except:
        return None


def filter_category_by_start_name(name):
    """
    Returns a category by its name.

    Args:
        name: (str): write your description
    """
    return Category.objects.filter(name__istartswith=name)


##################### ArticleCategory ##########################

def filter_article_category_by_article(a_id):
    """
    Returns an article by article id

    Args:
        a_id: (str): write your description
    """
    return ArticleCategory.objects.filter(article_id=a_id)


def filter_article_category_by_category(c_id):
    """
    Returns a list of the given category

    Args:
        c_id: (str): write your description
    """
    return ArticleCategory.objects.filter(category_id=c_id)


def get_or_create_article_category(a_id, c_id):
    """
    Gets an article object.

    Args:
        a_id: (str): write your description
        c_id: (str): write your description
    """
    return ArticleCategory.objects.get_or_create(article_id=a_id, category_id=c_id)


############# Tag ######################

def get_all_tag():
    """
    Get all tag objects.

    Args:
    """
    return Tag.objects.all()


def get_tag_by_id(id):
    """
    Get a tag by its id.

    Args:
        id: (int): write your description
    """
    try:
        return Tag.objects.get(id=id)
    except:
        return None


def filter_tag_by_start_name(name):
    """
    Filter tag by name.

    Args:
        name: (str): write your description
    """
    return Tag.objects.filter(name__istartswith=name)


def create_tag(name):
    """
    Create a tag

    Args:
        name: (str): write your description
    """
    return Tag.objects.create(name=name)


def get_or_create_tag(name):
    """
    Get an existing tag

    Args:
        name: (str): write your description
    """
    return Tag.objects.get_or_create(name=name)


def filter_tag_by_name_list(name):
    """
    Filter a list by name.

    Args:
        name: (str): write your description
    """
    return Tag.objects.filter(name__in=name)


def filter_tag_by_article(a_id):
    """
    Filter article by article_id.

    Args:
        a_id: (str): write your description
    """
    t_ids = list(filter_article_tag_by_article(a_id).values_list('tag_id', flat=True))
    if t_ids:
        return Tag.objects.filter(id__in=t_ids)
    else:
        return Tag.objects.none()


############# ArticleTag ######################

def filter_article_tag_by_article(a_id):
    """
    Filter article article article by article tag.

    Args:
        a_id: (str): write your description
    """
    return ArticleTag.objects.filter(article_id=a_id)


def filter_article_tag_by_tag(t_id):
    """
    Return a list of articletag by tag.

    Args:
        t_id: (str): write your description
    """
    return ArticleTag.objects.filter(tag_id=t_id)


def get_or_create_article_tag(a_id, t_id):
    """
    Get an article tag.

    Args:
        a_id: (str): write your description
        t_id: (str): write your description
    """
    return ArticleTag.objects.get_or_create(article_id=a_id, tag_id=t_id)


#################  Comment  #######################

def create_comment(nickname, email, content, article_id, root_id, to_id, type):
    """
    Create a comment

    Args:
        nickname: (str): write your description
        email: (str): write your description
        content: (str): write your description
        article_id: (str): write your description
        root_id: (str): write your description
        to_id: (str): write your description
        type: (str): write your description
    """
    return Comment.objects.create(nickname=nickname, email=email, content=content, article_id=article_id,
                                  root_id=root_id, to_id=to_id, type=type)


def filter_valid_comment_by_article(a_id):
    """
    Check if the comment is valid comment.

    Args:
        a_id: (str): write your description
    """
    return Comment.objects.filter(article_id=a_id, status__in=CommentStatusChoices.valid_choices())


def filter_created_comment():
    """
    Filter comment comment comment objects.

    Args:
    """
    return Comment.objects.filter(status=CommentStatusChoices.Created)


def get_comment_by_id(id):
    """
    Get comment by id

    Args:
        id: (str): write your description
    """
    try:
        return Comment.objects.get(id=id)
    except:
        return None


def get_valid_comment_by_id_and_article(id, a_id):
    """
    Return the comment with the given id

    Args:
        id: (int): write your description
        a_id: (str): write your description
    """
    try:
        return Comment.objects.get(id=id, article_id=a_id, status__in=CommentStatusChoices.valid_choices())
    except:
        return None


def all_comment():
    """
    Return all comments.

    Args:
    """
    return Comment.objects.all()


#################  FlatPage  #######################

def create_flatpage(title, content):
    """
    Create a flat flat page.

    Args:
        title: (str): write your description
        content: (str): write your description
    """
    return FlatPage.objects.create(title=title, content=content)


def get_flatpage_by_id(id):
    """
    Get a flat page by id.

    Args:
        id: (int): write your description
    """
    try:
        return FlatPage.objects.get(id=id)
    except:
        return None


def get_flatpage_by_url(url):
    """
    Get a page by url.

    Args:
        url: (str): write your description
    """
    try:
        FlatPage.objects.get(url=url)
    except:
        return None


def all_flatpage():
    """
    Returns a page objects.

    Args:
    """
    return FlatPage.objects.all()
