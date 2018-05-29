import json
from ast import literal_eval
from pprint import pprint, pformat

from django.db.models import TextField
from django.forms import Textarea
from froala_editor.fields import FroalaField

from app.ex_fields.widgets import MFroalaEditor, ConfigWidget


class MFroalaField(FroalaField):

    def formfield(self, **kwargs):
        if self.use_froala:
            widget = MFroalaEditor(options=self.options, theme=self.theme, plugins=self.plugins,
                                   include_jquery=self.include_jquery, image_upload=self.image_upload,
                                   file_upload=self.file_upload)
        else:
            widget = Textarea()
        defaults = {'widget': widget}
        defaults.update(kwargs)
        return super(FroalaField, self).formfield(**defaults)


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
