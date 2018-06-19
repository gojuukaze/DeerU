"""
生成html
"""
from tool.deeru_exceptions import NotSupportedError
from django.utils.html import format_html


class Tag(object):
    semicolon = ['style']
    space = ['class']

    extra_close_tag = ['br', 'hr']

    def __init__(self, name, text='', attrs=None):
        if attrs is None:
            attrs = {}

        self.name = name

        self.children = []
        self.text = text
        self.attrs = attrs

    @classmethod
    def get_tag_from_bs(cls, soup):
        from bs4 import BeautifulSoup as bs
        from bs4.element import Tag as bs_tag
        father = None
        if isinstance(soup, bs):
            father = soup.find()
        elif isinstance(soup, bs_tag):
            father = soup
        if not father or not father.name:
            return None

        tag = cls(father.name, father.text, father.attrs)

        for c in father.children:
            c_tag = cls.get_tag_from_bs(c)
            tag.append(c_tag)
        return tag

    @classmethod
    def get_tag_from_str(cls, html):
        from bs4 import BeautifulSoup as bs

        html = html.replace('\n', '')

        soup = bs(html, 'html.parser')
        return cls.get_tag_from_bs(soup)

    def append(self, tag):
        """
        添加子tag
        :return:
        """
        if not tag:
            return
        if not isinstance(tag, Tag):
            raise TypeError("添加的标签必须是 类Tag的对象")
        self.children.append(tag)

    def set_attr(self, name, value):
        self.attrs[name] = value

    def append_attrs_value(self, name, value):
        """
        属性追加值
        :param name:
        :param value:
        :return:
        """
        if name in self.semicolon:
            separator = ';'
        elif name in self.space:
            separator = ' '
        else:
            raise NotSupportedError("属性 %s 不支持追加值，找不到对应的分隔符，需要修改Tag类" % name)

        old_value = self.attrs.get('name', '').strip()

        if old_value and not old_value.endswith(separator):
            old_value += separator

        self.attrs[name] = old_value + value

    def __str__(self):

        children_html = ''.join(str(c) for c in self.children)
        close = '' if self.name in self.extra_close_tag else '</%s>' % self.name
        attrs_html = ' '.join('%s="%s"' % (k, v) if v else '' for k, v in self.attrs.items())
        return '<%s %s>%s %s %s' % (self.name, attrs_html, self.text, children_html, close)

    def format_html(self):
        return format_html(str(self))
