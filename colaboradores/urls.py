from django.urls import path
from . import views

app_name = 'colaboradores'

urlpatterns = [
    path('lista/', views.lista_colaboradores, name='lista'),
    path('novo/', views.novo_colaborador, name='novo'),
    path('editar/<int:pk>/', views.editar_colaborador, name='editar'),
    path('excluir/<int:pk>/', views.excluir_colaborador, name='excluir'),
]
