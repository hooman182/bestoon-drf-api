from django.db import models
from django.contrib.auth import get_user_model

# ------------------------------------------------------------------------

User = get_user_model()


class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="category")
    collection = models.ForeignKey(
        "collection.Collection", on_delete=models.CASCADE, related_name="income"
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.DecimalField(max_digits=12, decimal_places=3)
    date = models.DateField()

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
