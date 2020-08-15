from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponsePermanentRedirect
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout
from .models import Quiz, Question
from random import sample
# from .forms import QuestionForm
# Create your views here.


def quest(request):
    context = {
                # 'form': QuestionForm(),
                'amount': range(1,int(request.GET['amount'])+1),
                'qtitle': request.GET['title'],
                'qcat': request.GET['category'],
                'qamount': request.GET['amount']
              }
    if request.method == "POST":
        quiz_title = request.POST['qtitle']
        quiz_amount = request.POST['qamount']
        quiz_category = request.POST['qcat']
        quiz = Quiz(
            title=quiz_title,
            author=request.user.username,
            question_quantity=quiz_amount,
            category=quiz_category
            )
        quiz.save()
        for question in context['amount']:
            quest = str(question)
            tit = 'title' + quest
            title = request.POST[tit]
            an1 = '1ans'+quest
            ans1 = request.POST[an1]
            an2 = '2ans'+quest
            ans2 = request.POST[an2]
            an3 = '3ans'+quest
            ans3 = request.POST[an3]
            correct_answer_query = 'correct'+quest
            correct_answer_number = request.POST[correct_answer_query]
            correct_answer_cell = str(correct_answer_number)+'ans'+quest
            correct_answ_itself = request.POST[correct_answer_cell]
            quiz_question = Question(
                                        title=title,
                                        quiz_id=quiz.id,
                                        ans1=ans1,
                                        ans2=ans2,
                                        ans3=ans3,
                                        correct_ans=correct_answ_itself
                                    )
            quiz_question.save()
            return HttpResponsePermanentRedirect(f'quiz-info?quizid={quiz.id}')
    return render(request, 'Quiz/create-questions.html', context)


def create(request):
    return render(request, 'Quiz/create-quiz.html')


def warn(request):
    if 'quizid' in request.GET:
        quiz = Quiz.objects.get(id=request.GET['quizid'])
        context = {
                    'quiz': quiz
                  }
    return render(request, 'Quiz/warning.html', context)


def info(request):
    if "quizid" in request.GET:
        try:
            quizz = Quiz.objects.get(id=request.GET['quizid'])
        except Quiz.DoesNotExist:
            quizz = None
        context = {
                    'quiz': quizz,
                    'quizid': request.GET['quizid']
                }
    return render(request, 'Quiz/info.html', context)


def categ(request):
    context = {
                'errors': [],
                'math': len(Quiz.objects.filter(category="Math")),
                'logic': len(Quiz.objects.filter(category="Logic")),
                'biology': len(Quiz.objects.filter(category="Biology")),
                'sociology': len(Quiz.objects.filter(category="Sociology")),
                'fun': len(Quiz.objects.filter(category="Fun")),
                'geography': len(Quiz.objects.filter(category="Geography")),
                'history': len(Quiz.objects.filter(category="History")),
                'economic': len(Quiz.objects.filter(category="Economic")),
                }
    return render(request, 'Quiz/thematics.html', context)


def loggt(request):
    logout(request)
    return redirect('start')


def main(request):
    context = {
                'quizes': Quiz.objects.all()[::-1][:8],
                'funq': Quiz.objects.filter(category='Fun')[::-1][:4],
                'mathq': Quiz.objects.filter(category='Math')[::-1][:4],
                'geogrq': Quiz.objects.filter(category='Geography')[::-1][:4],
                'bioq': Quiz.objects.filter(category='Biology')[::-1][:4],
                'econoq': Quiz.objects.filter(category='Economic')[::-1][:4],
                'hisq': Quiz.objects.filter(category='History')[::-1][:4],
                'logq': Quiz.objects.filter(category='Logic')[::-1][:4],
                'socq': Quiz.objects.filter(category='Sociology')[::-1][:4],
                'filtered': None
              }
    if 'filter' in request.GET:
        filter = request.GET['filter']
        context = {
                        'filtered': Quiz.objects.filter(category=filter),
                        'filter': filter,
                        'quizes': None
                    }
        print(context['quizes'])
    return render(request, 'Quiz/main.html', context)


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
            return redirect('main')
        else:
            context['errors'].append("Invalid login or password!")
    return render(request, "Quiz/login.html", context)


def start(request):
    return render(request, 'Quiz/start.html')