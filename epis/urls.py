from django.urls import path
from . import views

urlpatterns = [
    # EPIs - manter apenas rotas de EPI aqui (o include do projeto já trata 'epis/')
    path('lista/', views.epi_lista, name='epi_lista'),
    path('novo/', views.epi_novo, name='epi_novo'),
    path('editar/<int:id>/', views.epi_editar, name='epi_editar'),
    path('excluir/<int:id>/', views.epi_excluir, name='epi_excluir'),
]
