from django.contrib import admin

# Register your models here.
from .models import *


class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')
    list_display_links = ('id', 'text')


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'action', 'score', 'result')
    list_display_links = ('id', 'action')


class ScoresAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'max_score', 'cur_score')
    list_display_links = ('id', 'user')


class ChapterAdmin(admin.ModelAdmin):
    list_display = ('id', 'page')
    list_display_links = ('id', 'page')


class AnnotationAdmin(admin.ModelAdmin):
    list_display = ('id', 'annot_id', 'text')
    list_display_links = ('id', 'annot_id', 'text')


class TermAdmin(admin.ModelAdmin):
    list_display = ('id', 'word')
    list_display_links = ('id', 'word')


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'choice')
    list_display_links = ('id', 'name', 'choice')


admin.site.register(Page, PageAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Scores, ScoresAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Annotation, AnnotationAdmin)
admin.site.register(Term, TermAdmin)
admin.site.register(Item, ItemAdmin)
