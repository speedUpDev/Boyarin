from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Page(models.Model):
    text = models.TextField()
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    description = models.CharField(max_length=600)
    last = models.BooleanField()

    def next_page(self):
        return self.id + 1

    def prev_page(self):
        return self.id - 1


class Choice(models.Model):
    page = models.ForeignKey('Page', on_delete=models.PROTECT, null=True)
    chapterId = models.IntegerField()
    action = models.TextField()
    result = models.BooleanField()
    score = models.IntegerField()
    result_text = models.TextField(default='')


class Scores(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', blank=True, null=True)
    max_score = models.IntegerField(default=0)
    cur_score = models.IntegerField(default=0)
    last_chapter = models.ForeignKey('Chapter', on_delete=models.PROTECT, null=True)
    progress = models.IntegerField(default=0)
    passed = models.BooleanField(default=False)
    last_choice = models.ForeignKey('Choice', on_delete=models.CASCADE, null=True, default=None)


class Chapter(models.Model):
    page = models.ForeignKey('Page', on_delete=models.PROTECT, null=True)

    def next_chapter(self):
        return self.id + 1

    def prev_chapter(self):
        return self.id - 1


class Annotation(Page):
    annot_id = models.IntegerField()

    def next_annotation(self):
        return self.annot_id + 1

    def prev_annotation(self):
        return self.annot_id - 1
