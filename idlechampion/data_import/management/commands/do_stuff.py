from django.core.management.base import BaseCommand

from data_import.models.meta_data import MetaDataRepository
from data_import.service.convert_game_data import ConvertGameData
from data_import.service.convert_user_data import ConvertUserData


class Command(BaseCommand):
    help = 'Stuff'

    def handle(self, *args, **options):
        ConvertGameData.generate_potions_from_game_data()
