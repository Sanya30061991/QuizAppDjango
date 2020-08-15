from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm, Textarea, TextInput
from .models import Quiz, Question


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


# class QuestionForm(ModelForm):
#     class Meta:
#         model = Question
#         fields = [
#                     'quiz_id',
#                     'title',
#                     'ans1',
#                     'ans2',
#                     'ans3',
#                     'correct_ans'
#                  ]
#         widgets = {
#                     'quiz_id': TextInput(attrs={
#                         'type': 'hidden'
#                     }),
#                     'title': TextInput(attrs={
#                         'name': 'title{{question}}',
#                         'type': "text",
#                         'class': "el",
#                         'placeholder': "{{question}} question",
#                         'required': ''
#                     }),
#                     'ans1': TextInput(attrs={
#                         'name': "1ans{{question}}",
#                         'type':"text",
#                         'class':"ans",
#                         'placeholder':"1 answer",
#                         'required': ''
#                     }),
#                     'ans2': TextInput(attrs={
#                         'name': "2ans{{question}}",
#                         'type':"text",
#                         'class':"ans",
#                         'placeholder':"2 answer",
#                         'required': ''
#                     }),
#                     'ans3': TextInput(attrs={
#                         'name': "3ans{{question}}",
#                         'type':"text",
#                         'class':"ans",
#                         'placeholder':"3 answer",
#                         'required': ''
#                     }),
#                     'correct_ans': TextInput(attrs={
#                         'class': "el",
#                         'type': "number",
#                         'name': "correct{{question}}",
#                         'min': "1",
#                         'max': "3",
#                         'placeholder': "0",
#                         'required': ''
#                     })
#                   }