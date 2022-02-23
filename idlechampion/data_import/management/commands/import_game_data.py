from django.core.management.base import BaseCommand

from data_import.service.convert_game_data import ConvertGameData
from data_import.service.import_data import ImportDataService


class Command(BaseCommand):
    help = 'Import Game Data'

    def handle(self, *args, **options):
        ImportDataService.import_game_data()
        ConvertGameData.generate_heroes_from_game_data()