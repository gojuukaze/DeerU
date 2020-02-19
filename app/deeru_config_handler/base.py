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
        return '%s:"%s"' % (self.__class__, self.args)


def deeru_config_handler(name):
    def deco(cls):
        setattr(cls, 'deeru_config_handler_name', name)
        return cls

    return deco