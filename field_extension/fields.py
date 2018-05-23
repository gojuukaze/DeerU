from django.forms import Textarea
from froala_editor.fields import FroalaField

from field_extension.widgets import KFroalaEditor


class KFroalaField(FroalaField):

    def formfield(self, **kwargs):
        if self.use_froala:
            widget = KFroalaEditor(options=self.options, theme=self.theme, plugins=self.plugins,
                                   include_jquery=self.include_jquery, image_upload=self.image_upload,
                                   file_upload=self.file_upload)
        else:
            widget = Textarea()
        defaults = {'widget': widget}
        defaults.update(kwargs)
        return super(FroalaField, self).formfield(**defaults)

