from django.core.management.base import BaseCommand

from data_import.service.convert_user_data import ConvertUserData
from data_import.service.import_data import ImportDataService
from data_import.service.update_data import UpdateData


class Command(BaseCommand):
    help = 'Import User Data'

    def handle(self, *args, **options):
        print('#####')
        print('Downloading Data')
        ImportDataService.import_user_data()
        print('#####')
        print('Unlock Heroes')
        ConvertUserData.unlock_heroes()
        print('#####')
        print('Update Loot')
        ConvertUserData.update_all_loot()
        print('#####')
        print('Update Potions')
        ConvertUserData.update_all_potion()
        print('#####')
        print('Compute Hero Data')
        UpdateData.update_hero_data()
        print('#####')
        print('Compute MetaData')
        UpdateData.update_metadata()
