# fs = FileSystemStorage(location='/media/photos')
from django.db import models
from django.utils.translation import ugettext as _

__all__ = ['Album']


class Album(models.Model):
    class Meta:
        verbose_name = _('图片')
        verbose_name_plural = _('图片')

    name = models.CharField(verbose_name=_('文件名'), max_length=50, blank=True)

    # photo = models.ImageField(storage=fs)
    img = models.ImageField(verbose_name=_('图片'))
