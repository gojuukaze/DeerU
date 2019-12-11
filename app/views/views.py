import json
from urllib import parse

from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseNotAllowed, JsonResponse, HttpResponseForbidden, HttpResponseRedirect, QueryDict
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import requires_csrf_token

from app.db_manager.config_manager import get_config_by_id
from app.db_manager.content_manager import get_article_meta_by_article, get_article_by_id
from app.db_manager.other_manager import create_image, get_all_image, \
    get_image_by_id
from app.forms import CommentForm
from app.manager import get_base_context
from app.manager.config_manager import get_theme
from app.manager.content_manager import is_valid_comment

theme = get_theme()


@requires_csrf_token
def page_not_found_view(request, exception):
    return render(request, theme + '/404.html', get_base_context({}))


@permission_required('app', raise_exception=True)
def upload_image_view(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['GET', 'POST'])
    file = request.FILES.get('file')
    try:
        from PIL import Image as pil_image
        pil_image.open(file).verify()
    except:
        if not file.name.endswith('.svg'):
            return JsonResponse({'error': '无法识别图片'})

    album = create_image(file.name, file)

    return JsonResponse({'msg': '上传成功!', 'link': album.img.url})


@permission_required('app', raise_exception=True)
def get_album(request):
    images = get_all_image().order_by('-id')
    return JsonResponse(
        [{'tag': 'img', "url": i.img.url, "thumb": i.img.url, 'id': i.id, 'name': i.img.name} for i in images],
        safe=False)


@permission_required('app', raise_exception=True)
def delete_image(request):
    id = request.POST.get('id', 0)
    try:
        get_image_by_id(id).delete()
    except:
        return HttpResponseForbidden()
    return JsonResponse({})


def create_comment(request):
    http_referer = request.META.get('HTTP_REFERER')
    if not http_referer:
        return HttpResponseForbidden()
    if request.method == 'POST':

        form = CommentForm(request.POST)

        if form.is_valid():
            article_id = form.cleaned_data['article_id']
            path = parse.urlparse(http_referer).path
            a_id = path.split('/')[-1]
            if int(article_id) != int(a_id):
                return HttpResponseForbidden()

            anchor = request.POST.get('err_anchor', '')

            success, msg = is_valid_comment(form)
            if not success:
                return HttpResponseRedirect(
                    reverse('app:detail_article', args=(article_id,)) + '?form_error=' + msg + anchor)
            # article_meta.comment_num += 1
            # article_meta.save()
            comment = form.save()
            anchor = request.POST.get('success_anchor', '')
            anchor += str(comment.id)
            return HttpResponseRedirect(reverse('app:detail_article', args=(article_id,)) + anchor)
        else:
            anchor = request.POST.get('err_anchor', '')
            article_id = form.cleaned_data['article_id']
            return HttpResponseRedirect(
                reverse('app:detail_article', args=(article_id,)) + '?form_error=' + '验证码错误' + anchor)


@permission_required('app', raise_exception=True)
def get_config_html(request, config_id):
    config = get_config_by_id(config_id)
    return render(request, 'app/admin/config.html',
                  {'schema': config.v2_schema,
                   'value': json.dumps(config.v2_config),
                   'script': config.v2_script})
