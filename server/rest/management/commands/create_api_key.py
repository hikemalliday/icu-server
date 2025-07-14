from django.core.management.base import BaseCommand
from rest_framework_api_key.models import APIKey


# Example usage: python manage.py create_api_key "my-client-app"
class Command(BaseCommand):
    help = "Create API key for client"

    def add_arguments(self, parser):
        parser.add_argument("name", type=str, help="A name to identify the API key owner")

    def handle(self, *args, **options):
        name = options["name"]
        _, key = APIKey.objects.create_key(name=name)

        self.stdout.write(self.style.SUCCESS(f"API Key for '{name}' created successfully!"))
        self.stdout.write(f"Name: {name}")
        self.stdout.write(f"Key: {key}")
