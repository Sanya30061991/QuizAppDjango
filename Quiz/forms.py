from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm, Textarea, TextInput


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = [
                    'username',
                    'email',
                    'password',
                 ]
        widgets = {
                    'username': TextInput(attrs={
                                                'class': "text",
                                                'type': "text",
                                                'name': "username",
                                                'placeholder': "Username",
                                                'required':""
                                                }),
                    'email': TextInput(attrs={
                                                'class': "text email",
                                                'type': "email",
                                                'name': "email",
                                                'placeholder': "Email",
                                                'required':""
                                                }),
                    'password': TextInput(attrs={
                                                'class': "text",
                                                'type': "password",
                                                'name': "password",
                                                'placeholder': "Password",
                                                'required':""
                                                })
                  }