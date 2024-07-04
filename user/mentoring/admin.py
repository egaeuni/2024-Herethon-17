from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Mento)
admin.site.register(Question)

class MentoAdmin(admin.ModelAdmin):
    list_display = ('Name',)