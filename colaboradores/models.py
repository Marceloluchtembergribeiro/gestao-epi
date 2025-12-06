from django.db import models


class Colaborador(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=14, unique=True)
    setor = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
