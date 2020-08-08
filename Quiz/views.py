from django.shortcuts import render

# Create your views here.
def registration(request):
    return render(request, "Quiz/registration.html")

def login(request):
    return render(request, "Quiz/login.html")