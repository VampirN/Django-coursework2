from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='mari.vampir@yandex.ru',
            company='Admin',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('123qwe')
        user.save()