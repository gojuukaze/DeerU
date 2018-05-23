from app.app_models.config_model import Config


def get_config_by_name(name):
    try:
        return Config.objects.get(name=name)
    except:
        return None