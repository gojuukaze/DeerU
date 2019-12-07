from django.core.management import BaseCommand
from django.core.management.utils import get_random_secret_key

from tool.version_upgrade.v1_config_to_v2 import config_v1_to_v2


class Command(BaseCommand):
    """
    用来临时跑一些东西
    python manage.py gen_secret_key
    """

    def handle(self, *args, **options):
        print("SECRET_KEY = '%s'" % get_random_secret_key())
