from django.core.management.base import BaseCommand, CommandError
import os


class Command(BaseCommand):
    help = "Create django app"

    def add_arguments(self, parser):
        parser.add_argument("app_name", type=str, help="App name")

    def handle(self, *args, **options):
        app_name = options["app_name"]
        os.system(
            "cd apps && python ../manage.py startapp" + " " + app_name + "&& cd .."
        )
        self.stdout.write("done")
