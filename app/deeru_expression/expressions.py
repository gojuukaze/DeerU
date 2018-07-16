import re

from tool.deeru_exceptions import ExpressionTypeError


class BaseExpression(object):
    result = None

    def __init__(self, args):
        """
        如：fa | xxx
        xxx是args
        :param args:
        """
        self.args = args
        self.result = None

    def calculate(self):
        """
        获取结果，要重写
        :return:
        """
        pass

    def get_result(self):
        """
        返回表达式的处理结果，类型不固定
        :return:
        """
        if not self.result:
            self.result = self.calculate()
        return self.result

    def __str__(self):
        return '%s:"%s"' % (self.__class__, self.args)


def get_attrs(args):
    """

    :param args: list
    :return:
    """
    attrs = {}
    for temp in args:
        k, v = temp.split('=')
        attrs[k.strip()] = v.strip()
    return attrs


class Img(BaseExpression):
    """
    img表达式
    {% img| src/id/name = xx [|其他属性] %}

    {% img|src= xx %}

    从图库中选取图片：

    {% img|id= 1 %}          --> 匹配 id

    {% img|name= xx %}          --> 匹配 name.startswith('xx')

    {% img|id=xx | style= xx %}

    返回
    {
        "type":'img',
        "src":'xxx',
        "attrs":{
            "style":'xx',
        }

    }
    """

    def calculate(self):
        from app.db_manager.other_manager import get_image_by_id, filter_image_by_start_name
        if not self.args:
            self.args = ''

        args = self.args.split('|')

        if len(args) == 0:
            raise ExpressionTypeError('表达式 text 至少需要一个参数')

        src = ''
        args_src = args[0]
        k, v = args_src.split('=')
        k = k.strip()
        v = v.strip()
        if k == 'src':
            src = v
        elif k == 'id':
            img = get_image_by_id(v)
            if img:
                src = img.img.url
        elif k == 'name':
            try:
                img = filter_image_by_start_name(v)[0]
                src = img.img.url
            except:
                pass
        if len(args) > 1:

            attrs = get_attrs(args[1:])
        else:
            attrs = {}

        return {
            'type': 'img',
            'src': src,
            'attrs': attrs
        }


class Svg(BaseExpression):
    """
    svg图片

    {% svg | <svg>...</svg> [|其他属性] %}

    返回
    {
        "type":'svg',
        "svg":'<svg>...</svg>'
        "attrs":{
            "style":'xx'
        }
    }
    """

    def calculate(self):
        if not self.args:
            self.args = ''

        args = self.args.split('|')

        if len(args) == 0:
            raise ExpressionTypeError('表达式 text 至少需要一个参数')

        svg = args[0]
        if len(args) > 1:
            attrs = get_attrs(args[1:])
        else:
            attrs = {}
        return {
            'type': 'svg',
            'svg': svg,
            'attrs': attrs
        }


class Fa(BaseExpression):
    """
    fontawesome图标表达式

    {% fa| fas xx [|其他属性] %}

    {% fa|fas xx %}
    {% fa|fas xx|style=  color:xx; %}

    返回
    {
        "type":'fa',
        "class_":'fas xxx',
        "attrs":{
            "style":'xx',
        }

    }
    """

    def calculate(self):
        if not self.args:
            self.args = ''
        args = self.args.split('|')

        if len(args) == 0:
            raise ExpressionTypeError('表达式 text 至少需要一个参数')

        class_ = args[0]
        if len(args) > 1:
            attrs = get_attrs(args[1:])
        else:
            attrs = {}

        return {
            'type': 'fa',
            'class': class_,
            'attrs': attrs
        }


class Cat(BaseExpression):
    """
    分类表达式
    {% cat| 值 | 返回值 name/url %}

    {% cat| xx | name %} --> 匹配：id=xx 或 name.startswith(xx) 返回name
    {% cat| name = xx | name %} --> 匹配name.startswith(xx) 返回name
    {% cat| id = xx | url %} --> 匹配id=xx 返回url

    """

    def calculate(self):
        from app.db_manager.content_manager import get_category_by_id, filter_category_by_start_name
        if not self.args:
            self.args = ''
        self.args = self.args.strip()

        if re.search(r'\|', self.args):
            temp_args = self.args.split('|')
            temp_args[-1] = temp_args[-1].strip()
            if temp_args[-1] not in ['name', 'url']:
                raise ExpressionTypeError('表达式 cat 最后一个参数仅支持 ["name","url"]')
            category = None
            if re.search(r'=', temp_args[0]):
                k, v = temp_args[0].split('=')
                k = k.strip()
                v = v.strip()
                if k == 'id':
                    category = get_category_by_id(v)
                elif k == 'name':
                    category = filter_category_by_start_name(v)[0]
            else:
                v = temp_args[0].strip()
                category = get_category_by_id(v)
                if not category:
                    category = filter_category_by_start_name(v)[0]
        else:
            raise ExpressionTypeError('表达式 cat 至少需要一个参数')

        if not category:
            return ''

        if temp_args[-1] == 'name':
            return category.name
        elif temp_args[-1] == 'url':
            return category.url()


class Tag(BaseExpression):
    """
    标签表达式
    {% tag| 值 | 返回值 name/url %}

    {% tag| xx | name %} --> 匹配：id=xx 或 name.startswith(xx) 返回name
    {% tag| name = xx | name %} --> 匹配name.startswith(xx) 返回name
    {% tag| id = xx | url %} --> 匹配id=xx 返回url

    """

    def calculate(self):
        from app.db_manager.content_manager import get_tag_by_id, filter_tag_by_start_name
        if not self.args:
            self.args = ''
        self.args = self.args.strip()

        if re.search(r'\|', self.args):
            temp_args = self.args.split('|')
            temp_args[-1] = temp_args[-1].strip()
            if temp_args[-1] not in ['name', 'url']:
                raise ExpressionTypeError('表达式 tag 最后一个参数仅支持 ["name","url"]')
            tag = None
            if re.search(r'=', temp_args[0]):
                k, v = temp_args[0].split('=')
                k = k.strip()
                v = v.strip()
                if k == 'id':
                    tag = get_tag_by_id(v)
                elif k == 'name':
                    tag = filter_tag_by_start_name(v)[0]
            else:
                v = temp_args[0].strip()
                tag = get_tag_by_id(v)
                if not tag:
                    tag = filter_tag_by_start_name(v)[0]
        else:
            raise ExpressionTypeError('表达式 tag 至少需要一个参数')

        if not tag:
            return ''

        if temp_args[-1] == 'name':
            return tag.name
        elif temp_args[-1] == 'url':
            return tag.url()


class Text(BaseExpression):
    """
    分类表达式
    {% text| 值 [| 其他属性] %}

    {% text| 1122 %}
    {% text| 1122 | style="color:red;" %}

    返回
    {
        "text":'xx',
        "attrs":{
            "style":'xx',
        }

    }

    """

    def calculate(self):
        if not self.args:
            self.args = ''
        args = self.args.split('|')

        if len(args) == 0:
            raise ExpressionTypeError('表达式 text 至少需要一个参数')

        text = args[0]
        if len(args) > 1:
            attrs = get_attrs(args[1:])
        else:
            attrs = {}

        return {
            'text': text,
            'attrs': attrs
        }
