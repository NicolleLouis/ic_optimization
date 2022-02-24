from django.core.management.base import BaseCommand

from data_import.models.hero import Hero


class Command(BaseCommand):
    help = 'Stuff'

    def handle(self, *args, **options):
        heroes = Hero.objects.all()
        list(map(
            lambda hero: hero.update_values(),
            heroes
        ))
