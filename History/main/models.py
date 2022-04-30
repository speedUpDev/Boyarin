from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Page(models.Model):
    text = models.TextField(verbose_name="Текст")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    description = models.CharField(max_length=600)
    last = models.BooleanField()

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'

    def __str__(self):
        return "Страница " + str(self.id)

    def next_page(self):
        return self.id + 1

    def prev_page(self):
        return self.id - 1


class Choice(models.Model):
    page = models.ForeignKey('Page', on_delete=models.PROTECT, null=True)
    chapterId = models.IntegerField()
    action = models.TextField(verbose_name="Действие")
    result = models.BooleanField(verbose_name="Продолжает игру")
    score = models.IntegerField(verbose_name="Очки")
    result_text = models.TextField(default='')

    class Meta:
        verbose_name = 'Выбор'
        verbose_name_plural = 'Выборы'

    def __str__(self):
        return str(self.chapterId) + ") " + self.action[:30]


class Scores(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', blank=True, null=True)
    max_score = models.IntegerField(default=0, verbose_name="Максимальный счет")
    cur_score = models.IntegerField(default=0, verbose_name="Текущий счет")
    last_chapter = models.ForeignKey('Chapter', on_delete=models.PROTECT, null=True)
    progress = models.IntegerField(default=0)
    passed = models.BooleanField(default=False)
    last_choice = models.ForeignKey('Choice', on_delete=models.CASCADE, null=True, default=None)
    dictionary = models.ManyToManyField('Term')
    items = models.ManyToManyField('Item')

    class Meta:
        verbose_name = 'Счет пользователя'
        verbose_name_plural = 'Счет пользователей'

    def __str__(self):
        return self.user.username


class Chapter(models.Model):
    page = models.ForeignKey('Page', on_delete=models.PROTECT, null=True, verbose_name="Страница")

    class Meta:
        verbose_name = 'Глава'
        verbose_name_plural = 'Главы'

    def __str__(self):
        return "Глава " + str(self.id)

    def next_chapter(self):
        return self.id + 1

    def prev_chapter(self):
        return self.id - 1


class Term(models.Model):
    word = models.TextField(verbose_name="Термин")
    description = models.TextField(verbose_name="Определение")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name="Изображение")
    source = models.TextField(blank=True, verbose_name="Источник")

    class Meta:
        verbose_name = 'Термин'
        verbose_name_plural = 'Термины'

    def __str__(self):
        return self.word


class Annotation(Page):
    annot_id = models.IntegerField(verbose_name="Id аннотации")

    class Meta:
        verbose_name = 'Аннотация'
        verbose_name_plural = 'Аннотации'

    def __str__(self):
        return "Аннотация " + str(self.annot_id)

    def next_annotation(self):
        return self.annot_id + 1

    def prev_annotation(self):
        return self.annot_id - 1


class Item(models.Model):
    name = models.TextField(verbose_name="Название")
    text = models.TextField(verbose_name="Описание")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name="Изображение")
    points = models.IntegerField(verbose_name="Очки", default=0)
    choice = models.ForeignKey('Choice', on_delete=models.CASCADE, blank=True, default=None)

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

    def __str__(self):
        return self.name
