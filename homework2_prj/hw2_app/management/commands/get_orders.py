from django.core.management.base import BaseCommand
from hw2_app.models import Order, Client, Product


class Command(BaseCommand):
    help = 'Get client orders'

    def add_arguments(self, parser):
        parser.add_argument('id_client', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        id_client = kwargs.get('id_client')
        orders = Order.objects.filter(client_id=id_client)
        for order in orders:
            self.stdout.write(f'{order} - {order.id}')
            # for product in order.products:
            #     self.stdout.write(f'\t{product.name} {product.price}')
