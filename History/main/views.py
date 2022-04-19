from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from .forms import LoginUserForm, RegisterUserForm
from .models import *


def index(request):
    button = ''

    if request.user.is_authenticated:
        if Scores.objects.filter(user=request.user).exists():
            score = Scores.objects.get(user=request.user)
            if score.cur_score == 0:
                button = 'Начать игру'
            else:
                button = 'Продолжить'
        else:
            Scores.objects.create(user=request.user, last_chapter=Chapter.objects.get(id=1))
            score = Scores.objects.get(user=request.user)
            button = 'Начать играть'
        return render(request, 'index.html', {'title': "Главная", 'button': button, 'score': score})
    else:
        return render(request, 'index.html', {'title': "Главная", 'button': button})


def rules(request):
    return render(request, 'rules.html', {'title': "Правила"})


def chapter(request, chptId):
    score = Scores.objects.get(user=request.user)
    chpt = Chapter.objects.get(id=chptId)
    pages = Page.objects.get(id=chpt.page.id)
    choices = Choice.objects.filter(page=pages)
    if score.last_chapter.id > chptId:
        choices = None
    if score.passed:
        text = score.last_choice.result_text
        score.passed = False
        score.save()
        end_chapter = True
    else:
        text = pages.text
        end_chapter = False
    score.last_chapter = chpt
    score.save()

    return render(request, 'chapter.html',
                  {'choices': choices, 'page': pages, 'title': "Historical game", 'score': score, 'chapter': chpt,
                   'text': text, 'end_chapter': end_chapter})


def ChoiceView(request, chptId):
    choice = Choice.objects.get(id=request.POST.get('choice_id'))
    if not choice.result:
        return redirect('Endgame')
    score = Scores.objects.get(user=request.user)
    score.cur_score += choice.score
    score.last_choice = choice
    score.passed = True
    score.save()
    return HttpResponseRedirect(reverse('Chapter', args=[str(chptId)], ))


def end_game(request):
    score = Scores.objects.get(user=request.user)
    score.max_score = score.cur_score
    score.cur_score = 0
    score.last_chapter = Chapter.objects.get(id=1)
    score.last_choice = None
    score.save()
    return render(request, 'end.html')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'
    extra_context = {'title': 'Авторизация'}

    def get_success_url(self):
        return reverse_lazy('Home')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    extra_context = {'title': 'Регистрация'}

    def get_success_url(self):
        return reverse_lazy('login')


def logout_user(request):
    logout(request)
    return redirect('login')
