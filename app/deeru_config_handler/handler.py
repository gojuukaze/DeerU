from app.deeru_config_handler.base import BaseHandler, deeru_config_handler


@deeru_config_handler('v2_kv_handler')
class KVHandler(BaseHandler):
    """
    args结构：
    {
       '_handler': 'v2_kv_handler',
       'data':[
           {
              'key':'k1',
              'value':'v1',
           },
           ...
       ]
    }

    ==========

    解析后的结构：
    {
        'k1':'v1',

        ...
    }

    """

    def calculate(self):
        """
        解析结果，要重写
        :return:
        :rtype: dict
        """
        r = {}
        for i in self.args['data']:
            r[i['key']] = i['value']
        return r


@deeru_config_handler('v2_img_handler')
class ImgHandler(BaseHandler):
    """
    args结构：
    {
        '_handler': 'v2_img_handler',
        'type': 'src',
        'value': '/media/1.png'
    }

    ==========

    解析后的结构：
    {
        'type':'img',
        'src':'/media/1.png',


        ...
    }

    """

    def calculate(self):
        """
        解析结果，要重写
        :return:
        :rtype: dict
        """
        from app.db_manager.other_manager import get_image_by_id,filter_image_by_start_name

        r = self.args
        v = self.args['value'].strip()
        type = self.args['type']
        if type == 'src':
            r['type'] = 'img'
            r['src'] = v
        elif type == 'id':
            r['type'] = 'img'
            img = get_image_by_id(v)
            if img:
                r['src'] = img.img.url
            else:
                r['src'] = ''
        elif type == 'name':
            r['type'] = 'img'
            try:
                img = filter_image_by_start_name(v)[0]
                src = img.img.url
            except:
                src = ''
            r['src'] = src
        elif type == 'fa':
            r['type'] = 'fa'
            r['class'] = v
        elif type == 'svg':
            r['type'] = 'svg'
            r['svg'] = v
        return r


@deeru_config_handler('v2_url_handler')
class UrlHandler(BaseHandler):
    """
    args结构：
    {
        '_handler': 'v2_url_handler',
        'type': 'url',
        'value': '/category/1'
    }

    ==========

    解析后的结构：

    '/category/1'

    """

    def calculate(self):
        """
        解析结果，要重写
        :return:
        :rtype: dict
        """
        from app.db_manager.content_manager import get_category_by_id, filter_category_by_start_name, get_tag_by_id, \
            filter_tag_by_start_name

        v = self.args['value'].strip()
        if self.args['type'] == 'url':
            return v
        elif self.args['type'] == 'cat':
            category = get_category_by_id(v)
            if not category:
                try:
                    category = filter_category_by_start_name(v)[0]
                except:
                    category = None
            if category:
                return category.url()
            else:
                return ''
        elif self.args['type'] == 'tag':
            tag = get_tag_by_id(v)
            if not tag:
                try:
                    tag = filter_tag_by_start_name(v)[0]
                except:
                    tag = None
            if tag:
                return tag.url()
            else:
                return ''
