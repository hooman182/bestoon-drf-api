from django.db import models
from django.contrib.auth import get_user_model
#------------------------------------------------------

User = get_user_model()

class Collection(models.Model):
    class Currency(models.TextChoices):
        IRR = "IRR", "ریال"
        TOMAN = "IRT", "تومان"
        DOLLAR = "USD", "دلار"

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="collection"
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    currency = models.CharField(
        max_length=20, choices=Currency.choices, default=Currency.TOMAN
    )

    def __str__(self) -> str:
        return self.title
