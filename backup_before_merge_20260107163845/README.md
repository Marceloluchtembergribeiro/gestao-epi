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
## Testes

```powershell
python manage.py test
```

## Docker (usando docker-compose)

Exemplo usando `docker-compose.yml` (arquivo na raiz do projeto):

1. Construa e suba os serviços:

```bash
docker compose up --build
```

2. O serviço web ficará exposto na porta `8000` (http://localhost:8000).

Observações:
- O `docker-compose.yml` inclui um serviço Postgres e monta a pasta `./backend` no container `web`.
- Para produção, ajuste variáveis de ambiente, volumes e use um banco gerenciado ou imagens otimizadas.