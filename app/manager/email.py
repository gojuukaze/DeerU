import threading

from django.conf import settings
from django.core.mail import EmailMultiAlternatives, get_connection
from django.core.mail.backends.smtp import EmailBackend

from app.consts import v2_app_config_context
from app.db_manager.config_manager import get_config_by_name
from tool.secure import descrypt
from tool.sign import unsign


def _send(subject, message, recipient_list,
          email_config=None, html_message=None, fail_silently=False):
    if not email_config:
        blog_config = get_config_by_name(v2_app_config_context['v2_blog_config']).v2_real_config
        email_config = blog_config['email']

    username = email_config.get('username', None) or settings.EMAIL_HOST_USER
    password = email_config.get('password', None)
    if password:
        password = descrypt(unsign(password))
    else:
        password = settings.EMAIL_HOST_PASSWORD
    smtp = email_config.get('smtp', None) or settings.EMAIL_HOST
    port = email_config.get('port', None) or settings.EMAIL_PORT
    secure = email_config.get('secure', None)
    if not secure:
        if settings.EMAIL_USE_TLS:
            secure = 'tls'
        elif settings.EMAIL_USE_SSL:
            secure = 'ssl'
    if not username or not password or not smtp or not port:
        return

    kwargs = {
        'host': smtp,
        'port': port,
        'username': username,
        'password': password,
        'fail_silently': fail_silently

    }
    if secure == 'tls':
        kwargs['use_tls'] = True
    elif secure == 'ssl':
        kwargs['use_ssl'] = True

    connection = EmailBackend(**kwargs)
    mail = EmailMultiAlternatives(subject, message, username, recipient_list, connection=connection)
    if html_message:
        mail.attach_alternative(html_message, 'text/html')

    a= mail.send()
    print(a)


def send_mail(subject, message, recipient_list,
              email_config=None, html_message=None, fail_silently=False):
    t = threading.Thread(target=_send,
                         args=(subject, message, recipient_list, email_config, html_message, fail_silently))
    t.start()
