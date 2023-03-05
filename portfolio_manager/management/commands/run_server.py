from django.core.management.commands.runserver import Command as RunServerCommand
from django.core.management import call_command

class Command(RunServerCommand):
    help = 'Starts the development server with populated data'

    def handle(self, *args, **options):
        print("hola")
        call_command('populate')
        call_command('runserver')
