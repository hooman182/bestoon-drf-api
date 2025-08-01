from django.contrib import admin
from expense.models import Expense

# ------------------------------------------------------------------------


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ["title", "amount", "collection", "user"]
    list_filter = ["collection", "amount"]
    search_fields = ["title"]
