from django.contrib.auth.models import User
from django.shortcuts import render
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def registration(request):
    context = {
                'form': UserForm(),
                'errors': []
              }
    if request.method == "POST":
        try:
            user = User.objects.get(email=request.POST['email'])
        except User.DoesNotExist:
            user = None
        if user is not None:
            context['errors'].append('User with this login has been already registered!')
        else:
            if request.POST['password']==request.POST['password1']:
                new_user = User.objects.create_user(
                                                request.POST['email'],
                                                request.POST['email'],
                                                request.POST['password']
                                                )
                new_user.save()
            else:
                context['errors'].append("Passwords aren't equal!")
    return render(request, "Quiz/registration.html", context)


def log_in(request):
    context = {
                'errors': []
              }
    if request.method == "POST":
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            context['errors'].append("Logged successfully!")
        else:
            context['errors'].append("Invalid login or password!")
    return render(request, "Quiz/login.html", context)


def start(request):
    return render(request, 'Quiz/start.html')