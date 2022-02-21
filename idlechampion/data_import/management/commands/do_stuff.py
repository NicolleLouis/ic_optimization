from django.core.management.base import BaseCommand

from data_import.service.convert_data import ConvertData


class Command(BaseCommand):
    help = 'Stuff'

    def handle(self, *args, **options):
        ConvertData.generate_heroes_from_game_data()
