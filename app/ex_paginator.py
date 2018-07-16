from django.core.paginator import Paginator
from django.utils.html import format_html


class DeerUPaginator(Paginator):
    def __init__(self, object_list, per_page, current_page_num, orphans=0, allow_empty_first_page=True):
        super().__init__(object_list, per_page, orphans, allow_empty_first_page)
        self.current_page_num = current_page_num
        self.start_index = 1
        self.end_index = self.num_pages

    def get_page_list(self, number=None):
        """
        :return:
        """
        number = number or self.current_page_num
        result = [None, None, [], None, None]
        if number - 1 > 0:
            result[2].append(number - 1)
            result[1] = number - 1

        result[2].append(number)

        if number + 1 <= self.end_index:
            result[2].append(number + 1)
            result[3] = number + 1

        if len(result[2]) < 3 and number + 2 <= self.end_index:
            result[2].append(number + 2)
        if len(result[2]) < 3 and number - 2 >= 1:
            result[2] = [number - 2] + result[2]

        if number != 1:
            result[0] = 1
        if number != self.end_index:
            result[4] = self.end_index

        return result

    def get_page_html_list(self, number):
        """
        已过时
        :param number:
        :return:
        """
        page = self.get_page_list(number)
        html1 = [{'text': format_html('<span class="icon is-small"><i class="fas fa-angle-double-left"></i></span>'),
                  'disabled': '', 'is_current': ' ', 'href': ' '},
                 {'text': format_html('<span class="icon is-small"><i class="fas fa-angle-left"></i></span>'),
                  'disabled': '', 'is_current': ' ', 'href': ' '},
                 {'text': format_html('<span class="icon is-small"><i class="fas fa-angle-right"></i></span>'),
                  'disabled': '', 'is_current': ' ', 'href': ' '},
                 {'text': format_html('<span class="icon is-small"><i class="fas fa-angle-double-right"></i></span>'),
                  'disabled': '', 'is_current': ' ', 'href': ' '}]
        i = 0
        for p in page[:2] + page[-2:]:
            if p:
                html1[i]['href'] = '?page=%d' % (p,)
            else:
                html1[i]['href'] = 'javascript:void(0)'
                html1[i]['disabled'] = 'disabled'
            i += 1

        html2 = []
        for p in page[2]:
            html2.append({'text': '%d' % (p,), 'disabled': '',
                          'is_current': 'is-current' if p == number else ' ', 'href': '?page=%d' % (p,)})

        return html1[:2] + html2 + html1[-2:]
