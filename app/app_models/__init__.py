def get_field(name):
    """
    Returns the field of a given name.

    Args:
        name: (str): write your description
    """
    import importlib
    temp = name.split('.')

    module_name = '.'.join(temp[:-1])
    module = importlib.import_module(module_name)
    return getattr(module, temp[-1])

