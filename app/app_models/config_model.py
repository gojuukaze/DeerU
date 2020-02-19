from django.conf import settings
from django.db import models
from app.app_models import get_field
from jsonfield import JSONField
from app.ex_fields.fields import ConfigField, ConfigFieldV2

__all__ = ['Config', 'Version']


class Config(models.Model):
    class Meta:
        verbose_name = '配置'
        verbose_name_plural = '配置'

    name = models.CharField(verbose_name='配置名称', max_length=20, unique=True)
    # --
    # 下面三是v1配置，会在之后的版本升级中删除
    config = ConfigField(verbose_name='v1版配置', null=True)
    last_config = ConfigField(verbose_name='v1版旧配置', blank=True, null=True)
    cache = models.TextField(verbose_name='解析后的config', null=True, blank=True, editable=False)
    # --

    # v2新增
    v2_config = ConfigFieldV2(verbose_name='v2版配置', null=True, blank=True, dump_kwargs={'ensure_ascii': False})

    # 经过handler处理后的配置，v2_config中的配置有的需要经过handler解析后才能使用
    # 保存配置时会自动处理v2_config并把结果保存到这
    v2_real_config = JSONField(verbose_name='解析后的config', null=True, blank=True, editable=False,
                               dump_kwargs={'ensure_ascii': False})

    v2_schema = models.TextField(verbose_name='json-editor配置', null=True, blank=True)
    # v2_script：js代码，会添加到创建json-editor之后，用于自定义配置的ui等
    v2_script = models.TextField(verbose_name='js代码', default='')
    created_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    modified_time = models.DateTimeField(verbose_name="修改时间", auto_now=True)

    def set_post_save_flag(self, v):
        self.first_config_post_save = v

    def get_post_save_flag(self):
        return getattr(self, 'first_config_post_save', True)


class Version(models.Model):
    class Meta:
        verbose_name = '版本'
        verbose_name_plural = '版本'

    version = models.CharField('版本号', max_length=20, editable=False)

    created_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    modified_time = models.DateTimeField(verbose_name="修改时间", auto_now=True)
