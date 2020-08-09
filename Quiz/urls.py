from django.urls import path
from . import views
urlpatterns = [
    path('', views.start),
    path('register', views.registration),
    path('auth', views.log_in),
]