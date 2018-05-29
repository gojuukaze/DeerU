from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseNotAllowed, JsonResponse, HttpResponseForbidden, HttpResponseRedirect, QueryDict
from django.urls import reverse

from app.db_manager.content_manager import get_article_meta_by_article, get_article_by_id
from app.db_manager.other_manager import create_image, get_all_image, \
    get_image_by_id
from app.forms import CommentForm


@permission_required('app', raise_exception=True)
def upload_image(request):
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

    images = get_all_image()
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
    if request.method == 'POST':

        form = CommentForm(request.POST)
        if form.is_valid():
            article_id = form.cleaned_data['article_id']
            article = get_article_by_id(article_id)

            if not article:
                msg = '错误id'
                return HttpResponseRedirect(
                    reverse('app:detail_article', args=(article_id,)) + '?form_error=' + msg + '#comment')
            # article_meta.comment_num += 1
            # article_meta.save()
            form.save()

            return HttpResponseRedirect(reverse('app:detail_article', args=(article_id,)) + '#comment')
