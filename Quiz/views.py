from django.contrib.auth.models import User
from django.shortcuts import render
from .forms import UserForm
# Create your views here.
def registration(request):
    context = {
                'form': UserForm(),
                'errors': []
              }
    if request.method == "POST":
        try:
            user = User.objects.get(username=request.POST['username'])
        except User.DoesNotExist:
            user = None
        if user is not None:
            context['errors'].append('User with this login has been already registered!')
        else:
            if request.POST['password']==request.POST['password1']:
                new_user = User.objects.create_user(' ', request.POST['email'], request.POST['password'])
                new_user.save()
            else:
                context['errors'].append("Passwords aren't equal!")
    return render(request, "Quiz/registration.html", context)

def login(request):
    context = {
                'form': UserForm(),
                'errors': []
              }
    return render(request, "Quiz/login.html")