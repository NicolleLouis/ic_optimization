from django.core.management.base import BaseCommand

from data_import.service.convert_user_data import ConvertUserData


class Command(BaseCommand):
    help = 'Stuff'

    def handle(self, *args, **options):
        ConvertUserData.update_all_loot()
