from django.contrib import admin
from .models import *

admin.site.register(Mento)
admin.site.register(Question)
admin.site.register(Record)

class MentoAdmin(admin.ModelAdmin):
    list_display = ('Name',)