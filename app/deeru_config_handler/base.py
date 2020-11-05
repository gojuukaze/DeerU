class BaseHandler(object):
    result = None

    def __init__(self, args):
        """
        :param args:
        :type args:dict

        """
        self.args = args
        self.result = None

    def calculate(self):
        """
        解析结果，要重写
        :return:
        """
        pass

    def get_result(self):
        """

        :return:
        :rtype: dict
        """
        if not self.result:
            self.result = self.calculate()
        return self.result

    def __str__(self):
        """
        Return a string representation of this class.

        Args:
            self: (todo): write your description
        """
        return '%s:"%s"' % (self.__class__, self.args)


def deeru_config_handler(name):
    """
    Decorator to register a class.

    Args:
        name: (str): write your description
    """
    def deco(cls):
        """
        Decorator to add an attribute.

        Args:
            cls: (todo): write your description
        """
        setattr(cls, 'deeru_config_handler_name', name)
        return cls

    return deco