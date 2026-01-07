FROM python:3.11-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
COPY . /app
RUN python -m venv .venv && . .venv/bin/activate && pip install --upgrade pip && pip install django
WORKDIR /app/backend
EXPOSE 8000
CMD ["/bin/sh", "-c", ". .venv/bin/activate && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('colaboradores/', include('colaboradores.urls')),
    path('epis/', include('epis.urls')),  # <-- ADICIONADO: expõe /epis/lista/
]

{% extends "admin/base.html" %}<!-- deve ser a PRIMEIRA coisa no arquivo -->
{% block title %}Gestão de EPIs — Administração{% endblock %}

{% block content %}
  <div class="container">
    <h1>Gestão de EPIs</h1>
    <p>Área administrativa personalizada.</p>
  </div>
{% endblock %}
