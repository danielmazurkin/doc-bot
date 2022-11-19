from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, username: str, password: str, **extra_fields):
        if not password:
            raise ValueError(_("Пароль должен быть задан"))
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_authorization", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(username, password, **extra_fields)

    def get_by_tg_id(self, tg_id: str):
        return self.get(telegram_id=tg_id)

    def get_or_none(self, *args, **kwargs):
        try:
            return self.get(*args, **kwargs)
        except ObjectDoesNotExist:
            return None
