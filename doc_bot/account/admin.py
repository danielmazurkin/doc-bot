from django.contrib import admin
from django.contrib.auth.models import Group

from account.models import User


@admin.register(User)
class UserProfileAdmin(admin.ModelAdmin):
    search_fields = (
        "name",
    )

    fieldsets = (
        (
            "Пользователь бота",
            {
                "fields": (
                    "name",
                )
            },
        ),
    )

    list_display = (
        "telegram_id",
        "name",
        "date_joined",
    )

    def get_queryset(self, request):
        qs = None
        if request.user.is_superuser:
            qs = User.objects.filter(is_superuser=False)
        return qs

    def has_add_permission(self, request):
        return False


admin.site.unregister(Group)
