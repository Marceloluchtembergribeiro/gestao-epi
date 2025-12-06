# Projeto Gestão EPI - instruções rápidas

1. Entrar na pasta backend:
   cd C:\EPIs\gestao-epi\backend

2. Ativar virtualenv:
   .\.venv\Scripts\Activate.ps1

3. Instalar dependências (se houver requirements.txt):
   pip install -r requirements.txt

4. Criar e aplicar migrações:
   python manage.py makemigrations
   python manage.py migrate

5. Criar superuser (opcional):
   python manage.py createsuperuser

6. Rodar servidor:
   python manage.py runserver

7. Acessos:
   - Lista de colaboradores: http://127.0.0.1:8000/colaboradores/lista/
   - Admin: http://127.0.0.1:8000/admin/