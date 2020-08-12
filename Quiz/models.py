from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Quiz(models.Model):
    title = models.TextField('Title of entire quiz')
    author = models.TextField('Login of an author')
    question_quantity = models.IntegerField('Amount of available questions')
    category = models.TextField('Category of this quiz')