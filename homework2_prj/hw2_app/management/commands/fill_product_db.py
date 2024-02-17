from django.core.management.base import BaseCommand
from hw2_app.models import Product
from random import choice, choices, random, randint
from string import ascii_uppercase as letters, digits
from django.utils import lorem_ipsum

names = ['apple', 'honor', 'huawei', 'samsung', 'xiaomi', 'sony']
gb = ['64', '128', '256', '512']


class Command(BaseCommand):
    help = 'Create fake products database.'

    def handle(self, *args, **kwargs):
        for _ in range(20):
            product = Product(
                name=((choice(names).capitalize() + ' ' +
                               ''.join(choices(letters, k=3)) + '-' +
                               ''.join(choices(digits, k=2))) + '/' +
                              choice(gb) + 'Gb'),
                description='\n'.join(lorem_ipsum.paragraphs(1, common=False)),
                price=round(random() * 10000, 2),
                product_count=randint(1, 50),
                added_at=f'202{randint(0, 3)}-0{randint(1, 9)}-{randint(10, 28)}',
            )
            product.save()
            self.stdout.write(f'{product}')
