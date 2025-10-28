from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, default='user')  # admin or user
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
