import bleach
from bleach.sanitizer import Cleaner
from bs4 import BeautifulSoup

COMMENT_ALLOWED_TAGS = [
    'a',
    'p',
    'span',
    'strong',
    'pre',
    's',
    'u',
    'em',
    'br'
]
COMMENT_ALLOWED_ATTRIBUTES = {
    'a': ['href', 'target', 'rel'],
    'span': ['style'],
}

COMMENT_ALLOWED_STYLES = ['color', 'background-color']

COMMENT_ALLOWED_PROTOCOLS = ['http', 'https', 'mailto', 'data']


def clean_all_tags(html_doc):
    cleaner = Cleaner(tags=[], attributes={}, styles=[], protocols=[], strip=True)
    return cleaner.clean(html_doc)


def get_safe_comment_html(html_doc):
    cleaner = Cleaner(tags=COMMENT_ALLOWED_TAGS, attributes=COMMENT_ALLOWED_ATTRIBUTES, styles=COMMENT_ALLOWED_STYLES,
                      protocols=COMMENT_ALLOWED_PROTOCOLS, strip=False)
    return cleaner.clean(html_doc)


def add_link(html_doc):
    return bleach.linkify(html_doc)


def clean_all_tags_and_get_img(html_doc):
    """
    清理所有标签，
    将html_doc中的img 标签替换为"图片"两个文字 ，获取纯文本

    :param html_doc:
    :return:
    """
    soup = BeautifulSoup(html_doc)
    img_src = None  # 图片的地址
    for image_tag in soup.find_all('img'):
        image_tag.string = ''
        tmp_src = image_tag['src']
        if img_src is None and tmp_src.startswith('http'):
            img_src = tmp_src

    return soup.text, img_src


def get_text_from_html_doc(html_doc):
    soup = BeautifulSoup(html_doc)
    return soup.text
