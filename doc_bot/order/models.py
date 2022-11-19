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

    def __str__(self):
        return f"Заказа номер: {self.number}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


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
