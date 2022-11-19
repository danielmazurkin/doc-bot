from django.utils import timezone

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from account.managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    """Модель описывающая таблицу телеграм пользователя."""

    email = None

    username = models.CharField(
        null=True, blank=True, max_length=255, verbose_name="Логин", unique=True
    )
    name = models.CharField(
        verbose_name="Имя Фамилия", blank=False, null=True, max_length=100
    )
    telegram_id = models.BigIntegerField(
        unique=True,
        verbose_name="Уникальный id в Телеграм",
        null=True,
    )

    date_joined = models.DateTimeField(
        verbose_name="Дата регистрации", default=timezone.now
    )


    is_staff = models.BooleanField(
        verbose_name="Владелец услуги",
        default=False,
    )
    is_active = models.BooleanField(
        verbose_name="Суперадмин",
        default=True,
    )
    is_authorization = models.BooleanField(
        verbose_name="Пользователь бота",
        default=False,
    )

    USERNAME_FIELD = "username"

    objects = CustomUserManager()

    class Meta:
        verbose_name = "Пользователь бота"
        verbose_name_plural = "Пользователи бота"
