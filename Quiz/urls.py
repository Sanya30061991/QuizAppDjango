from django.urls import path
from . import views
urlpatterns = [
    path('', views.start, name='start'),
    path('register', views.registration),
    path('auth', views.log_in),
    path('list', views.main, name="main"),
    path('log-out', views.loggt, name="logout"),
    path('thematics', views.categ, name="categories"),
    path('quiz-info', views.info, name="information")
]