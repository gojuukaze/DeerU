from pprint import pprint

from django.core.management import BaseCommand

from app.app_models.content_model import Article
from app.manager.manager import get_category_for_choice

from wordcloud import WordCloud
import matplotlib.pyplot as plt


class Command(BaseCommand):
    """
    用来临时跑一些东西
    python manage.py temp
    """

    def handle(self, *args, **options):
        s='as aa bb as w as w dd dd df ghf e'
        wordcloud = WordCloud().generate(s)
        print(type(wordcloud))
        plt.figure()

        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()



