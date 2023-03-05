from django.core.management.base import BaseCommand
from portfolio_manager.utils.create_models_from_excel import populate_data

class Command(BaseCommand):
    help = 'Populate data from Excel file'

    def handle(self, *args, **options):
        populate_data()
        self.stdout.write(self.style.SUCCESS('Data successfully populated!'))
