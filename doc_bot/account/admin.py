from django.contrib import admin
from django.contrib.auth.models import Group

from account.models import User


@admin.register(User)
class UserProfileAdmin(admin.ModelAdmin):
    search_fields = (
        "name",
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


admin.site.unregister(Group)
