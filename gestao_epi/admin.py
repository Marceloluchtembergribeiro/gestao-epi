from django.contrib import admin
from colaboradores.models import Colaborador
from epis.models import EPI


class GestaoEPIAdminSite(admin.AdminSite):
    site_header = "Gestão EPI — Administração"
    site_title = "Gestão EPI Admin"
    index_title = "Painel Administrativo"

    def index(self, request, extra_context=None):
        extra = extra_context or {}
        extra.update({
            "colaboradores_count": Colaborador.objects.count(),
            "epis_count": EPI.objects.count(),
            "recent_colaboradores": Colaborador.objects.order_by('-id')[:5],
            "recent_epis": EPI.objects.order_by('-id')[:5],
        })
        return super().index(request, extra_context=extra)


gestao_admin = GestaoEPIAdminSite(name="gestao_admin")
