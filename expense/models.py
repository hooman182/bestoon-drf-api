from django.contrib.auth import get_user_model
from django.db import models

from categories.models import Category
from collection.models import Collection

# --------------------------------------------------------------

User = get_user_model()


class Expense(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="expense",
    )
    collection = models.ForeignKey(
        Collection,
        on_delete=models.CASCADE,
        related_name="expense",
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.DecimalField(max_digits=12, decimal_places=3)
    date = models.DateField()
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name="expense",
        blank=True,
        null=True,
    )

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
