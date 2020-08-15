from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Quiz(models.Model):
    title = models.TextField('Title of entire quiz')
    author = models.TextField('Login of an author')
    question_quantity = models.IntegerField('Amount of available questions')
    category = models.TextField('Category of this quiz') # History, Math, Logic, Fun, Biology, Geography, Sociology, Economic
    total = models.IntegerField('Total amount of user passes through this quiz', default=0)


class Question(models.Model):
    quiz_id = models.IntegerField('ID of related quiz')
    title = models.TextField('Title of exact question')
    ans1 = models.CharField('1 possible answer', max_length=100)
    ans2 = models.CharField('2 possible answer', max_length=100)
    ans3 = models.CharField('3 possible answer', max_length=100)
    correct_ans = models.CharField('Correct answer to this question', max_length=100)


class Result(models.Model):
    quiz_id = models.IntegerField('ID of passed quiz')
    user_id = models.IntegerField("ID of user, who has passed")
    result = models.IntegerField("Amount of right answers", default=0)
    quiz_name = models.CharField("Name of passed quiz", max_length=100, default="test")
    quiz_category = models.CharField("Category of passed quiz", max_length=100, default="test")
    quiz_amount = models.IntegerField("Amount of questions of passed quiz", default=0)