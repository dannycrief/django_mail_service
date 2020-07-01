from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import EmailIHistory
from django.forms import ModelForm


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class SendEmailForm(ModelForm):
    class Meta:
        model = EmailIHistory
        fields = ['user', 'receiver', 'title', 'message', 'date_of_send']
