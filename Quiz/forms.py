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
                    'first_name'
                 ]
        widgets = {
                    'username': TextInput(attrs={

                                                }),
                    'email': TextInput(attrs={

                                                }),
                    'password': TextInput(attrs={

                                                }),
                    'first_name': TextInput(attrs={

                                                }),
                  }