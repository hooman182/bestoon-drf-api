from django.contrib import admin

from .models import Income


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ["title", "amount", "collection","user"]
    list_filter = ["user", "amount"]
    search_fields = ["user"]
