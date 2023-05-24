# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    extra = models.JSONField(default=dict, blank=True, null=True)
    USERNAME_FIELD = 'username'