import json
from ast import literal_eval

from django.db.models import TextField

from jsonfield import JSONField

from app.ex_fields.widgets import ConfigWidget, ConfigWidgetV2


class ConfigField(TextField):

    def to_python(self, value):
        """
        Convert value to json.

        Args:
            self: (todo): write your description
            value: (str): write your description
        """
        value = super().to_python(value)
        if not value:
            return value
        value = literal_eval(value)
        return json.dumps(value, ensure_ascii=False, indent=4)

    def formfield(self, **kwargs):
        """
        Returns a default form field.

        Args:
            self: (todo): write your description
        """
        defaults = {'widget': ConfigWidget,
                    'max_length': self.max_length}
        defaults.update(kwargs)
        defaults['widget'] = ConfigWidget
        return super(TextField, self).formfield(**defaults)


class ConfigFieldV2(JSONField):

    def formfield(self, **kwargs):
        """
        Returns the formfield for this field.

        Args:
            self: (todo): write your description
        """
        defaults = {'widget': ConfigWidgetV2}
        defaults.update(kwargs)
        defaults['widget'] = ConfigWidgetV2
        return super().formfield(**defaults)
