
def get_base_context(context):
    from app.manager.config_manager import get_global_value, get_theme_config
    from app.manager.uiconfig_manager import get_top_menu, get_aside_category2, get_aside_tags, get_top_ico

    context['top_menu'] = get_top_menu()
    context['global_value'] = get_global_value()
    context['aside_category'] = get_aside_category2()
    context['aside_tags'] = get_aside_tags()
    context['top_ico'] = get_top_ico()
    context['theme_config'] = get_theme_config()

    return context