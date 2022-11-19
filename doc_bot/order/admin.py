from django.contrib import admin
from django.contrib.admin import TabularInline

from order.models import Order, Document


# Register your models here.
class DocumentFileInline(TabularInline):
    model = Document
    fields = ("file",)
    verbose_name = "Документ для печати"
    verbose_name_plural = "Документы для печати"
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Админка для модели Заказ"""

    list_display = (
        "number",
        "user",
    )

    search_fields = ["number"]

    inlines = [
        DocumentFileInline,
    ]

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "number",
                    "user",
                )
            },
        ),
    )

    readonly_fields = (
        "user",
        "number",
    )

