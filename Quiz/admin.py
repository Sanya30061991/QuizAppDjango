from django.contrib import admin
from .models import Quiz, Question, UserResult
# Register your models here.

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(UserResult)