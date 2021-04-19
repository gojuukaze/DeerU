import json
from ast import literal_eval

from django.db.models import TextField
from django.forms import Textarea

from jsonfield import JSONField

from app.ex_fields.widgets import ConfigWidget, ConfigWidgetV2, DeerUFroalaEditor


class ConfigField(TextField):

    def to_python(self, value):
        value = super().to_python(value)
        if not value:
            return value
        value = literal_eval(value)
        return json.dumps(value, ensure_ascii=False, indent=4)

    def formfield(self, **kwargs):
        defaults = {'widget': ConfigWidget,
                    'max_length': self.max_length}
        defaults.update(kwargs)
        defaults['widget'] = ConfigWidget
        return super(TextField, self).formfield(**defaults)


class ConfigFieldV2(JSONField):

    def formfield(self, **kwargs):
        defaults = {'widget': ConfigWidgetV2}
        defaults.update(kwargs)
        defaults['widget'] = ConfigWidgetV2
        return super().formfield(**defaults)

from froala_editor.fields import FroalaField

class DeerUFroalaField(FroalaField):
    def formfield(self, **kwargs):
        if self.use_froala:
            widget = DeerUFroalaEditor(options=self.options, theme=self.theme, plugins=self.plugins,
                                  include_jquery=self.include_jquery, image_upload=self.image_upload,
                                  file_upload=self.file_upload, third_party=self.third_party)
        else:
            widget = Textarea()
        defaults = {'widget': widget}
        defaults.update(kwargs)
        return super(FroalaField, self).formfield(**defaults)
