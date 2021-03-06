from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required

from History.settings import STATIC_ROOT
from .forms import LoginUserForm, RegisterUserForm
from .models import *


def index(request):
    button = ''
    print(STATIC_ROOT)
    if request.user.is_authenticated:
        if Scores.objects.filter(user=request.user).exists():
            score = Scores.objects.get(user=request.user)
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


@login_required
def chapter(request, chptId):
    score = Scores.objects.get(user=request.user)
    chpt = Chapter.objects.get(id=chptId)
    pages = Page.objects.get(id=chpt.page.id)
    choices = Choice.objects.filter(page=pages)
    items = None
    text = pages.text
    end_chapter = False
    if score.last_chapter.id > chptId:
        choices = None
    if score.last_choice is not None:
        if not score.last_choice.result:
            return redirect('Endgame')
        if score.passed or score.last_choice.page == pages:
            items = Item.objects.filter(choice=score.last_choice)
            text = score.last_choice.result_text + f" <b>(+{str(score.last_choice.score)})</b>"
            score.passed = False
            score.save()
            end_chapter = True
    else:
        text = pages.text
        end_chapter = False
    score.last_chapter = chpt
    score.save()

    return render(request, 'chapter.html',
                  {'choices': choices, 'page': pages, 'title': f"Глава {chpt.id}", 'score': score, 'chapter': chpt,
                   'text': text, 'end_chapter': end_chapter, 'items': items})


@login_required
def ChoiceView(request, chptId):
    choice = Choice.objects.get(id=request.POST.get('choice_id'))
    score = Scores.objects.get(user=request.user)
    score.last_choice = choice
    score.save()
    if not choice.result:
        return redirect('Endgame')
    items = Item.objects.filter(choice=choice)

    for item in items:
        score.cur_score += item.points
        score.items.add(item)
    score.cur_score += choice.score
    score.passed = True
    score.save()
    return HttpResponseRedirect(reverse('Chapter', args=[str(chptId)], ))


@login_required
def annotation(request, annId):
    ann = Annotation.objects.get(annot_id=annId)
    score = Scores.objects.get(user=request.user)
    return render(request, 'annotation.html', {'annotation': ann, 'score': score, 'title': "Аннотация"})


@login_required
def end_game(request):
    score = Scores.objects.get(user=request.user)
    text = score.last_choice.result_text
    return render(request, 'end.html', {'title': "Поражение", 'text': text, 'score': score})


@login_required
def game_final(request):
    score = Scores.objects.get(user=request.user)
    if not score.last_chapter.page.last:
        return HttpResponseRedirect(reverse('Chapter', args=[str(score.last_chapter.id)], ))
    points = score.cur_score
    if points <= 20:
        text = "К сожалению, Вы так и остались отроком и не смогли дослужиться до более высокого положения при " \
               "княжеской дружине. Всё, что Вы видели на белом свете — это прислуживание и исполнение мелких " \
               "поручений, уборка еды со стола и ношение вещей за княжеской особой. "
    elif points <= 40:
        text = "В древнерусском обществе Вы смогли бы стать “детским” — младшим слугой князя, который выполнял бы его " \
               "мелкие поручения. В отличие от отрока, Вам было бы позволено даже владеть мечом, дабы в опасных " \
               "ситуациях суметь защитить князя или прийти к нему на помощь. "
    elif points <= 67:
        text = "Вы сумели достичь положения гриди. В отличие от отроков и детских, Вы входите в княжескую младшую " \
               "дружину и имеете доступ к особе князя в качестве его личного телохранителя. У таких как Вы даже есть " \
               "собственный кров над головой — гридницы! "
    elif points <= 90:
        text = "В Древней Руси Вас явно ждал бы успех! Вы смогли стать десятским в старшей дружине князя. Вы " \
               "управляйте небольшим, но крепким отрядом — костяком княжеской дружины. Со своими гридями Вы — " \
               "страшная сила на пути любого княжеского врага! "
    elif points <= 109:
        text = "Вы смогли достичь всего, о чем даже и мечтать не могли! За Вашим родом закрепляется должность " \
               "тысяцкого в одном из крупных городов Русской земли. Сами же Вы на некоторое время становитесь " \
               "посадником князя в другом большом поселении. У Вас есть свое жилье и дружина. Доходы текут рекой. " \
               "Сыновья пристроены при княжеском дворе, а дочерей Вы планируете выдать замуж за влиятельнейших бояр, " \
               "а того гляди и за князей Рюриковичей. Что и говорить, Вы — владетельный боярин эпохи удельной " \
               "раздробленности! "
    else:
        text = "Ошибка"
    if score.max_score < score.cur_score:
        score.max_score = score.cur_score
        score.save()
    return render(request, 'final.html', {'score': score, 'text': text, 'title': "Финал"})


@login_required
def dictionary(request):
    score = Scores.objects.get(user=request.user)
    words = score.dictionary.all()
    return render(request, 'dictionary.html', {'score': score, 'terms': words, 'title': "Словарь"})


@login_required
def items(request):
    score = Scores.objects.get(user=request.user)
    items = score.items.all()
    return render(request, 'items.html', {'score': score, 'items': items, 'title': "Трофеи"})


@login_required
def AppendDictView(request, termId):
    score = Scores.objects.get(user=request.user)
    term = Term.objects.get(id=termId)
    if not term in score.dictionary.all():
        score.dictionary.add(term)
    return redirect('Dictionary')


@login_required
def RestartView(request):
    score = Scores.objects.get(user=request.user)
    score.cur_score = 0
    score.last_chapter = Chapter.objects.get(id=1)
    score.items.clear()
    score.last_choice = None
    score.save()
    return redirect('Home')


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
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
