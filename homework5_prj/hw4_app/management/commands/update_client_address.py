from django.core.management.base import BaseCommand
from hw4_app.models import Client


class Command(BaseCommand):
    help = 'Update client address'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')
        parser.add_argument('new_data', type=str, help='New address')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        new_data = kwargs.get('new_data')
        client = Client.objects.filter(pk=pk).first()
        if client is not None:
            client.address = new_data
            client.save()
            self.stdout.write(f'{client} updated')
        else:
            self.stdout.write(f'Client with id {pk} not found')
