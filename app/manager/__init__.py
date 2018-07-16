def get_rich_text_filed(name):
    import importlib
    temp = name.split('.')

    module_name = '.'.join(temp[:-1])
    module = importlib.import_module(module_name)
    return getattr(module, temp[-1])


def get_config_context():
    from django.apps import apps
    import importlib
    from ast import literal_eval
    from app.db_manager.config_manager import get_config_by_name

    result = {}

    for app in apps.get_app_configs():
        deeru_config = getattr(app, 'deeru_config_context', None)
        if deeru_config:
            deeru_config = deeru_config.split('.')
            module_name = '.'.join(deeru_config[:-1])
            consts = importlib.import_module(module_name)
            app_config = getattr(consts, deeru_config[-1], {})
            for k, v in app_config.items():
                config = get_config_by_name(v)
                if config:
                    result[k] = literal_eval(config.cache)
    return result


def get_base_context(context):
    from app.manager.uiconfig_manager import get_aside_category2, get_aside_tags
    context['config'] = get_config_context()

    context['category'] = get_aside_category2()
    context['tags'] = get_aside_tags()

    return context
