import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'bjxu7l2-r*8ar0*#_s360e!jm#5cs$3pd%k(ooz5g*p!72j07t'

INSTALLED_APPS = [
    # admin扩展
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

    # deeru
    'app.apps.MAppConfig',
    'base_theme.apps.BaseThemeConfig',
    'deeru_cmd.apps.DeerUCmdConfig',
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

FLATPAGE_URL = '/p/'

# 富文本编辑器配置

DEERU_RICH_EDITOR = {
    'filed': 'app.ex_fields.fields.MFroalaField',
    'article_kwargs': {
        'options': {
            'height': 300,
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
            'height': 300,
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
LOG_DIR = os.path.join(BASE_DIR, 'log')
