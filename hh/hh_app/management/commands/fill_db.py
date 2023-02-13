from django.core.management.base import BaseCommand, CommandError
from hh.hh_app.models import Region, Skill, Vacancy

class Command(BaseCommand):
    def handle(self, *args, **options):
        print('This is my command!')