from django.core.management.base import BaseCommand
from hw4_app.models import Product


class Command(BaseCommand):
    help = 'Get products by name'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Product name')

    def handle(self, *args, **kwargs):
        search_product = kwargs.get('name')
        products = Product.objects.filter(name__icontains=search_product)
        for i, product in enumerate(products, start=1):
            self.stdout.write(f'{i}. {product}')
