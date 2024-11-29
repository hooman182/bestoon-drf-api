from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Category(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='category')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Collection(models.Model):

    class Currency(models.TextChoices):
        IRR = 'Rial', 'ریال'
        TOMAN = 'Toman', 'تومان'
        DOLLAR = 'USD', 'دلار'

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='expense')
    title = models.CharField(max_length=200)
    description = models.TextField()
    currency = models.CharField(
        max_length=20, choices=Currency.choices, default=Currency.TOMAN)

    def __str__(self) -> str:
        return self.title


class Expense(models.Model):
    collection = models.ForeignKey(
        Collection, on_delete=models.CASCADE, related_name='expense')
    title = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.DecimalField(max_digits=12, decimal_places=3)
    date = models.DateField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='expense')

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
