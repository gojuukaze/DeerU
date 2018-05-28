import os

from tool.deeru_expression.expressions import BaseExpression

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'bjxu7l2-r*8ar0*#_s360e!jm#5cs$3pd%k(ooz5g*p!72j07t'

INSTALLED_APPS = [
    'jet',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'froala_editor',
    'ktag.apps.KtagConfig',
    'app.ex_fields.apps.FieldExtensionConfig'

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'deeru.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'deeru.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

EXPRESSION = ['tool.deeru_expression.expressions']

from importlib import import_module

EXPRESSION_DICT = {}
for f in EXPRESSION:
    exp_mod = import_module(f)
    for name in dir(exp_mod):
        if name.startswith('_') or name == 'BaseExpression':
            continue
        try:
            _class = getattr(exp_mod, name)
            if isinstance(_class(None), BaseExpression):
                EXPRESSION_DICT[name.lower()] = _class
        except:
            pass

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [os.path.join(BASE_DIR, "theme/static"), ]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# jet主题
JET_DEFAULT_THEME = 'light-gray'

FROALA_EDITOR_PLUGINS = ('align', 'char_counter', 'code_beautifier', 'code_view', 'colors', 'draggable', 'emoticons',
                         'entities', 'file', 'font_family', 'font_size', 'fullscreen', 'image', 'image_manager',
                         'inline_style',
                         'line_breaker', 'link', 'lists', 'paragraph_format', 'paragraph_style', 'quick_insert',
                         'quote', 'save', 'table',
                         'url', 'video')
FROALA_EDITOR_OPTIONS = {
    'language': 'zh_cn',
    'imageUploadURL': '/image/upload',

    'imageAllowedTypes': ['jpeg', 'jpg', 'png', 'svg', 'bmp', 'gif'],
    'imageManagerPageSize': 5,
    'imageManagerLoadURL': "/images",

    'imageManagerDeleteURL': "/image/delete",
    'imageManagerDeleteMethod': "POST",
}
