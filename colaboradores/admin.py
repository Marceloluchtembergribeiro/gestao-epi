from django.contrib import admin
from .models import Colaborador


class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'setor')
    search_fields = ('nome', 'cpf', 'setor')


admin.site.register(Colaborador, ColaboradorAdmin)
