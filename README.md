# Gestão de EPIs - Projeto

Instruções:

1. Ativar ambiente:
   python -m venv .venv
   & .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt (ou pip install django)

2. Rodar:
   cd backend
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver

Docker: veja Dockerfile no repositório.
