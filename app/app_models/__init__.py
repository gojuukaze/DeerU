def get_field(name):
    import importlib
    temp = name.split('.')

    module_name = '.'.join(temp[:-1])
    module = importlib.import_module(module_name)
    return getattr(module, temp[-1])

