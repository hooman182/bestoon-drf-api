from django.db import models
from django.contrib.auth import get_user_model

from collection.models import Collection
from categories.models import Category

User = get_user_model()


class Expense(models.Model):
    collection = models.ForeignKey(
        Collection, on_delete=models.CASCADE, related_name="expense"
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.DecimalField(max_digits=12, decimal_places=3)
    date = models.DateField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="expense"
    )

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title