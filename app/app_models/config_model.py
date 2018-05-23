from django.db import models

from tool.kblog_model_field import ConfigField

__all__ = ['Config', 'UiConfig']


class Config(models.Model):
    class Meta:
        verbose_name = '配置'
        verbose_name_plural = '配置'

    name = models.CharField(verbose_name='配置名称', max_length=20, db_index=True, unique=True)
    config = ConfigField(verbose_name='配置')
    last_config = ConfigField(verbose_name='旧配置', blank=True)

    created_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    modified_time = models.DateTimeField(verbose_name="修改时间", auto_now=True)


class UiConfig(models.Model):
    class Meta:
        verbose_name = '界面配置'
        verbose_name_plural = '界面配置'

    name = models.CharField(verbose_name='配置名称', max_length=20, db_index=True, unique=True)
    config = ConfigField(verbose_name='配置')
    last_config = ConfigField(verbose_name='旧配置', blank=True)

    created_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    modified_time = models.DateTimeField(verbose_name="修改时间", auto_now=True)