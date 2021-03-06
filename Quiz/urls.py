from django.urls import path
from . import views
urlpatterns = [
    path('', views.start, name='start'),
    path('register', views.registration),
    path('auth', views.log_in),
    path('list', views.main, name="main"),
    path('log-out', views.loggt, name="logout"),
    path('thematics', views.categ, name="categories"),
    path('quiz-info', views.info, name="information"),
    path('warning', views.warn, name="warning"),
    path('create-quiz', views.create, name="creation"),
    path('create-quest', views.quest, name="quest"),
    path('passed', views.passed, name="passed"),
    path('pass-quiz', views.process, name="process"),
    path('user-result', views.result, name="result")
]