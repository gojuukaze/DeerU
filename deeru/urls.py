from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('froala_editor/', include('froala_editor.urls')),
    path('admin/doc/', include('django.contrib.admindocs.urls'))

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
