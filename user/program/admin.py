from django.contrib import admin
from .models import Program, Policy, Benefit

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'region', 'image')
    search_fields = ('title', 'region')

class BenefitInline(admin.TabularInline):
    model = Benefit
    extra = 1

@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    inlines = [BenefitInline]
    list_display = ('title',)
    search_fields = ('title',)