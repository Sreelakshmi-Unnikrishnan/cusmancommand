from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

#Positional Arguments
class Command(BaseCommand):
    help = 'Generate random users'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        for i in range(count):
            User.objects.create_user(username=get_random_string(5), email='hello@hi.com', password='123')

#Optional Arguments
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    help = 'Generate random users'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Indicates the number of users to be created')

        # Optional argument
        parser.add_argument('-p', '--prefix', type=str, help='Define a username prefix')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        prefix = kwargs['prefix']

        for i in range(count):
            if prefix:
                username = f'{prefix}_{get_random_string(4)}'
            else:
                username = get_random_string(3)
            User.objects.create_user(username=username, email='hello@hi.com', password='123')

#Boolean/Flag arguments
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    help = 'Generate random users'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Indicates the number of users to be created')
        parser.add_argument('-p', '--prefix', type=str, help='Define a username prefix')
        parser.add_argument('-s', '--superuser', action='store_true', help='Create a superuser account')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        prefix = kwargs['prefix']
        superuser = kwargs['superuser']

        for i in range(count):
            if prefix:
                username = f'{prefix}_{get_random_string(4)}'
            else:
                username = get_random_string(3)

            if superuser:
                User.objects.create_superuser(username=username, email='hello@hi.com', password='123')
            else:
                User.objects.create_user(username=username, email='hello@hi.com', password='123')