from django.apps import AppConfig


class MAppConfig(AppConfig):
    name = 'app'

    def ready(self):
        # signals are imported, so that they are defined and can be used
        import app.signals.handlers
