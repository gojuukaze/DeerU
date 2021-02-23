from django.http import HttpResponse, Http404

from app.db_manager.content_manager import get_article_by_id, get_category_by_id, \
    get_tag_by_id, get_flatpage_by_id

from app.manager.content_manager import get_flatpage_url_dict
from app.manager.theme import get_home_template, get_category_template, get_tag_template, get_detail_article_template, \
    get_detail_flatpage_template, get_404_template


def home_view(request):
    """
    """
    page = int(request.GET.get('page', 1))
    # per_page = int(request.GET.get('per_page', 7))
    t = get_home_template(page)

    return HttpResponse(t.get_html(request))


def category_article_list_view(request, category_id):
    """
    """
    page = int(request.GET.get('page', 1))
    category = get_category_by_id(category_id)
    if not category:
        raise Http404()
    t = get_category_template(category, page)

    return HttpResponse(t.get_html(request))


def tag_article_list_view(request, tag_id):
    """
    """
    page = int(request.GET.get('page', 1))
    tag = get_tag_by_id(tag_id)
    if not tag:
        raise Http404()
    t = get_tag_template(tag, page)

    return HttpResponse(t.get_html(request))


def detail_article_view(request, article_id):
    form_error = request.GET.get('form_error', '')
    article = get_article_by_id(article_id)
    if not article:
        raise Http404()
    meta_data = article.meta_data()
    meta_data.read_num += 1
    meta_data.save()
    t = get_detail_article_template(article, form_error)

    return HttpResponse(t.get_html(request))


def detail_flatpage_view(request, url):
    url_dict = get_flatpage_url_dict()
    try:
        page_id = url_dict[url]
    except:
        raise Http404()
    flatpage = get_flatpage_by_id(page_id)

    t = get_detail_flatpage_template(flatpage)

    return HttpResponse(t.get_html(request))


def page_not_found_view(request, exception):
    t = get_404_template()

    return HttpResponse(t.get_html(request))
