from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework.authtoken.models import Token


class User(AbstractUser):
    name = models.CharField(max_length=10)


class CustomUserToken(Token):
    user = models.OneToOneField('accounts.User', on_delete=models.CASCADE, related_name='token')
