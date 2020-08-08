from django.urls import path
from . import views
urlpatterns = [
    path('register', views.registration),
    path('auth', views.login)
]