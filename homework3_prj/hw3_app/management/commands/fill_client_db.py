from django.core.management.base import BaseCommand
from hw3_app.models import Client
from random import choice, randint
from django.utils import lorem_ipsum

mails = ['@yandex.ru', '@mail.ru', '@gmail.com', '@hotmail.com', '@outlook.com']


class Command(BaseCommand):
    help = 'Create fake clients database.'

    def handle(self, *args, **kwargs):
        for _ in range(15):
            client = Client(
                name=lorem_ipsum.words(1, common=False).capitalize() + ' ' +
                     lorem_ipsum.words(1, common=False).capitalize(),
                phone=f'+7({randint(100, 999)}){randint(100, 999)}-{randint(10, 99)}-{randint(10, 99)}',
                address=f'{lorem_ipsum.words(1, common=False).capitalize()} street, {randint(1, 200)}',
                registration_date=f'202{randint(0, 3)}-0{randint(1, 9)}-{randint(10, 28)}',
            )
            client.email = client.name[:5] + choice(mails)
            client.save()
            self.stdout.write(f'{client}')
