from random import choice

from django.db import models
from django.conf import settings


def user_directory_path(instance, filename):
    """Функция выдает путь к загруженному файлу"""
    return f"{instance.__class__.__name__}/user_{instance.user.id}/{filename}"


class Order(models.Model):
    """Модель заказа"""

    number = models.PositiveIntegerField(verbose_name="Номер заказа")

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name="order",
    )

    @classmethod
    def get_number(cls):
        number_order = settings.NUMBER_ORDER
        exist_number_order = cls.objects.all().values_list("number", flat=True)
        if exist_number_order.exists():
            random_number = choice(list(number_order.difference(list(exist_number_order))))
        else:
            random_number = choice(list(number_order))
        return random_number

    def __str__(self):
        return f"Заказа номер: {self.number}"

    class Meta:
        verbose_name = "Заказ на печать"
        verbose_name_plural = "Заказы на печать"


class Document(models.Model):
    """Модель для документов в модель Order"""

    file = models.FileField(
        upload_to=user_directory_path,
        verbose_name="Документ для печати",
    )

    user = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        verbose_name="Заказ клиента",
        related_name="document",
    )

    def __str__(self):
        return "Документ"
