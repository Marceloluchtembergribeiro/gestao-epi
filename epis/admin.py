from django.contrib import admin
from .models import EPI
from gestao_epi.admin import gestao_admin


class EPIAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ca')


admin.site.register(EPI, EPIAdmin)
gestao_admin.register(EPI, EPIAdmin)
