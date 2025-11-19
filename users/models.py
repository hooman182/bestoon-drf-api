from django.contrib.auth.models import AbstractUser
from django.db import models

from users.managers import CustomUserManager

#------------------------------------------------------

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self) -> str:
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name="profile"
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth = models.DateField(blank=True, null=True)
    
    bio = models.TextField(blank=True, null=True)
    
    address = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
        
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"