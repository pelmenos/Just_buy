from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

from shop.models import Cart


class CustomUserManager(BaseUserManager):
    def create_user(self, email, fio, password, **extra_fields):
        if not email:
            raise ValueError(_('The Email must be set'))
        if not fio:
            raise ValueError(_('The FIO must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, fio=fio, **extra_fields)
        user.is_active = True
        user.set_password(password)
        user.save()
        cart = Cart(user=user)
        cart.save()
        return user

    def create_superuser(self, email, fio, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, fio, password, **extra_fields)
