DEBUG = True

ALLOWED_HOSTS = ['*']

CUSTOM_EXPRESSION = []

CUSTOM_APPS = [
'deeru_qiniu.apps.DeeruQiniuConfig'
]

QINIU = {'access_key': 'tLwKefcf_tSSfRlha6WA2_tpgEeYNN3l7CB5jazL',
         'secret_key': 'zYHYNZEq6XpFa4tm7h6lhIm6gQcHWV2lAGVhm_38',
         'bucket_name': 'ikaze',
         'media_pre':'media',
         'static_pre': 'static'}

