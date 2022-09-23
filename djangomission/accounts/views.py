from django.shortcuts import render

# Create your views here.
from accounts.crud import user_login
from utils.mixin import CreateMixin


class UserLoginAPI(CreateMixin):
    creator = staticmethod(user_login)
