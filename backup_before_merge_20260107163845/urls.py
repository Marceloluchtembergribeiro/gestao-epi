from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render


def home(request):
    return render(request, "home.html")


urlpatterns = [
    path('', home, name='home'),  # <-- PÁGINA INICIAL
    path('admin/', admin.site.urls),
    path('colaboradores/', include('colaboradores.urls')),
    path('epis/', include('epis.urls')),
]
