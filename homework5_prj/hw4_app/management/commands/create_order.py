from django.core.management.base import BaseCommand
from hw4_app.models import Order, Client, Product
from random import randint, choice


class Command(BaseCommand):
    help = 'Create order'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Orders count')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        clients = Client.objects.all()
        products = Product.objects.all()

        for _ in range(count):
            client = choice(clients)
            order = Order(
                client=client,
                total_price=0,
                created_at=f'202{randint(0, 3)}-0{randint(1, 9)}-{randint(10, 28)}',
            )
            order.save()
            for _ in range(randint(1,5)):
                product = choice(products)
                self.stdout.write(f'{product}')
                order.products.add(product)
                order.total_price += product.price
                order.save()

            self.stdout.write(f'{order}')
