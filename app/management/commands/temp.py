from django.core.management import BaseCommand

from tool.version_upgrade.v1_config_to_v2 import config_v1_to_v2


class Command(BaseCommand):
    """
    用来临时跑一些东西
    python manage.py temp
    """

    def handle(self, *args, **options):
        config_v1_to_v2()



