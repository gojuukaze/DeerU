import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


INSTALLED_APPS = [
    # admin扩展
    'jet.dashboard',
    'jet',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admindocs',
    'django.contrib.sitemaps',
    # 分类排序
    'adminsortable2',
    # 富文本
    'froala_editor',
    # tag输入
    'ktag.apps.KtagConfig',
    # 验证码
    'captcha',

    # deeru
    'app.apps.MAppConfig',
    'base_theme.apps.BaseThemeConfig',
    'deeru_cmd.apps.DeerUCmdConfig',
    'deeru_dashboard.apps.DeeruDashboardConfig',
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

# jet后台
JET_DEFAULT_THEME = 'light-gray'
JET_SIDE_MENU_COMPACT = True
JET_INDEX_DASHBOARD = 'deeru_dashboard.dashboard.CustomIndexDashboard'

JET_SIDE_MENU_ITEMS = [
    {'label': '文章', 'app_label': 'app', 'items': [
        {'name': 'article'},
        {'name': 'category'},
        {'name': 'tag'},

    ]},
    {'label': '评论', 'app_label': 'app', 'items': [
        {'name': 'comment'},
    ]},
    {'label': '单页面', 'app_label': 'app', 'items': [
        {'name': 'flatpage'},
    ]},
    {'label': '媒体', 'app_label': 'app', 'items': [
        {'name': 'album'},
    ]},
    {'label': '配置', 'app_label': 'app', 'items': [
        {'name': 'config'},
    ]},
    {'label': '账户', 'app_label': 'auth', 'items': [
        {'name': 'user'},
    ]},
]

# 富文本编辑器
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
    'emoticonsUseImage': False,
}

###########################

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',
    }
}

# FROALA_INCLUDE_JQUERY = False

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATICFILES_DIRS = [os.path.join(BASE_DIR, "base_theme/static"), ]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# 表达式

EXPRESSION = ['app.deeru_expression.expressions']
CUSTOM_EXPRESSION = []

# handler
CONFIG_HANDLER = ['app.deeru_config_handler.handler']
CUSTOM_CONFIG_HANDLER = []

FLATPAGE_URL = '/p/'

# 富文本编辑器配置

DEERU_RICH_EDITOR = {
    'filed': 'froala_editor.fields.FroalaField',
    'article_kwargs': {
        'options': {
            'height': 350,
            'toolbarButtons': ['fontFamily', 'fontSize', 'color', '|', 'paragraphFormat',
                               'paragraphStyle', 'bold', 'italic', 'underline', 'strikeThrough',
                               '|', 'align', 'formatOL', 'formatUL', 'outdent', 'indent', '|',
                               'emoticons', 'insertLink', 'insertImage', 'insertVideo',
                               '-', 'insertTable', 'quote', 'insertHR', 'clearFormatting', 'undo',
                               'redo', 'html',
                               ],
        }
    },
    'flatpage_kwargs': {
        'options': {
            'height': 350,
            'toolbarButtons': ['fontFamily', 'fontSize', 'color', '|', 'paragraphFormat',
                               'paragraphStyle', 'bold', 'italic', 'underline', 'strikeThrough',
                               '|', 'align', 'formatOL', 'formatUL', 'outdent', 'indent', '|',
                               'emoticons', 'insertLink', 'insertImage', 'insertVideo',
                               '-', 'insertTable', 'quote', 'insertHR', 'clearFormatting', 'undo',
                               'redo', 'html',
                               ],
        }
    }
}

# log
LOG_DIR = ''

# 验证码
CAPTCHA_CHALLENGE_FUNCT = 'tool.captcha.math_challenge'
CAPTCHA_FONT_PATH = os.path.join(BASE_DIR, 'data/Alibaba-PuHuiTi-Regular.ttf')
CAPTCHA_FONT_SIZE = 17
CAPTCHA_NOISE_FUNCTIONS = ('tool.captcha.noise_arcs',)

