from django.core.management.base import BaseCommand

from to_do_list.models import Task


class Command(BaseCommand):
    help = 'Helps doing stuff'

    def handle(self, *args, **options):
        task = Task(name="Yes ma gueule")
        task.save()
