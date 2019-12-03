from app.app_models.config_model import Config


def get_config_by_name(name):
    """
    :rtype: Config
    """
    try:
        return Config.objects.get(name=name)
    except:
        return None


def get_config_by_id(id):
    """
    :rtype: Config
    """
    try:
        return Config.objects.get(id=id)
    except:
        return None
