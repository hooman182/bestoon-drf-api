from django.contrib import admin
from expense.models import Category, Collection, Expense


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    pass