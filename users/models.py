from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    '''Модель позьзователя (создателя рассылок)'''
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')
    company = models.CharField(unique=True, max_length=50, verbose_name='Название компании')
    avatar = models.ImageField(upload_to='users/', verbose_name='Фото', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE)
    country = models.CharField(max_length=25, verbose_name='Страна', **NULLABLE)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ("email",)
        permissions = [
            ("can_view_users_list", "can view users list"),
            ("can_block_user", "can block user"),
        ]