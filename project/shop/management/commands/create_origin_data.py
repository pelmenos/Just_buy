from django.core.management.base import BaseCommand, CommandError

from shop.models import Product
from user.models import CustomUser


class Command(BaseCommand):
    help = "Create origin data in bd"

    def handle(self, *args, **options):
        try:
            CustomUser.objects.create_superuser(email='admin@shop.ru', password='QWEasd123', fio='Ivanov Ivan Ivanovich')
            CustomUser.objects.create_user(email='user@shop.ru', password='password', fio='Sergeev Sergey Sergeevich')
            Product.objects.create(name='Lemon', description='Yellow Lemon', price='100')
            Product.objects.create(name='Orange', description='Orange orange', price='150')
            Product.objects.create(name='Apple', description='Green Apple', price='50')
        except Exception:
            raise CommandError('Data have already created')

        self.stdout.write(
            self.style.SUCCESS('Data was created')
        )
