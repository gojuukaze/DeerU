from django.apps import AppConfig


class MAppConfig(AppConfig):
    name = 'app'

    deeru_type = 'project'
    deeru_config_context = 'app.consts.app_config_context'

    def ready(self):
        # signals are imported, so that they are defined and can be used
        import app.signals.handlers
