from django.contrib.auth import get_user_model
from django.db import models
from datetime import datetime, timedelta
from django.utils import timezone

# ------------------------------------------------------

User = get_user_model()


class Collection(models.Model):

    class Currency(models.TextChoices):
        IRR = "IRR", "ریال"
        TOMAN = "IRT", "تومان"
        DOLLAR = "USD", "دلار"

    class CollectionType(models.TextChoices):
        INCOME = "INCOME", "درآمد"
        EXPENSE = "EXPENSE", "مخارج"

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="collection")
    title = models.CharField(max_length=200)
    description = models.TextField()

    currency = models.CharField(
        max_length=20, choices=Currency.choices, default=Currency.TOMAN
    )
    collection_type = models.CharField(
        max_length=20, choices=CollectionType.choices, default=CollectionType.EXPENSE
    )

    created = models.DateField(auto_now_add=True)
    deadline = models.DateField()

    EXPIRY_DAYS = 30
    
    def is_expired(self):
        return timezone.now().date() > self.deadline
    
    def save(self, *args, **kwargs):
        if not self.deadline:
            self.deadline = (self.created or timezone.now().date()) + timedelta(days=self.EXPIRY_DAYS)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title