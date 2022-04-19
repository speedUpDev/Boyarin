from django.conf.urls.static import static
from django.urls import path

from History import settings
from .views import *

urlpatterns = [
    path('', index, name="Home"),
    path('rules/', rules, name="Rules"),
    path('end/', end_game, name="Endgame"),
    path('chapter/<int:chptId>', chapter, name="Chapter"),
    path('choice/<int:chptId>', ChoiceView, name="Choice"),
    path('logout/', logout_user, name='logout'),
    path('login/', LoginUser.as_view(), {'title': 'Авторизация'}, name='login'),
    path('registration/', RegisterUser.as_view(), {'title': 'Регистрация'}, name="registration"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
