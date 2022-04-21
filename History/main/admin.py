from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Page)
admin.site.register(Choice)
admin.site.register(Scores)
admin.site.register(Chapter)
admin.site.register(Annotation)