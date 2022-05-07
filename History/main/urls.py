from django.conf.urls.static import static
from django.urls import path

from History import settings
from .views import *

urlpatterns = [
    path('', index, name="Home"),
    path('rules/', rules, name="Rules"),
    path('end/', end_game, name="Endgame"),
    path('dictionary/', dictionary, name="Dictionary"),
    path('trophies/', items, name="Trophies"),
    path('chapter/<int:chptId>', chapter, name="Chapter"),
    path('annotation/<int:annId>', annotation, name="Annotation"),
    path('choice/<int:chptId>', ChoiceView, name="Choice"),
    path('logout/', logout_user, name='logout'),
    path('chapter/append_dict/<int:termId>', AppendDictView, name='AppendDict'),
    path('final/', game_final, name='Final'),
    path('login/', LoginUser.as_view(), {'title': 'Авторизация'}, name='login'),
    path('registration/', RegisterUser.as_view(), {'title': 'Регистрация'}, name="registration"),
    path('restart', RestartView, name='restart'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
