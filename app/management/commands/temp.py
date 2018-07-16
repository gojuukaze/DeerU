from pprint import pprint

from django.core.management import BaseCommand

from app.app_models.config_model import Config
from app.app_models.content_model import Article
from app.manager.ct_manager import get_category_for_choice




class Command(BaseCommand):
    """
    用来临时跑一些东西
    python manage.py temp
    """

    def handle(self, *args, **options):
        for c in Config.objects.all():
            c.save()



