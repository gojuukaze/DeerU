from django.db import models

from app.ex_fields.fields import ConfigField

__all__ = ['Config',]


class Config(models.Model):
    class Meta:
        verbose_name = '配置'
        verbose_name_plural = '配置'

    name = models.CharField(verbose_name='配置名称', max_length=20, db_index=True, unique=True)
    config = ConfigField(verbose_name='配置')
    last_config = ConfigField(verbose_name='旧配置', blank=True)
    cache = models.TextField(verbose_name='解析后的config', null=True, blank=True, editable=False)

    created_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    modified_time = models.DateTimeField(verbose_name="修改时间", auto_now=True)

    def set_post_save_flag(self, v):
        self.first_config_post_save = v

    def get_post_save_flag(self):
        return getattr(self, 'first_config_post_save', True)

