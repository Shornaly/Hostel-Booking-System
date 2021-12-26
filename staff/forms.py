from django.contrib.auth.models import UserCreationForm
from django.contrib.auth.models import User
from django import forms
class CreateUser(UserCreationForm):
    class Meta:
        model=User
        fields=['email','password1']
