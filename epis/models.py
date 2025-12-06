from django.db import models


class Colaborador(models.Model):
    nome = models.CharField(max_length=200)
    matricula = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.nome} ({self.matricula})"


class EPI(models.Model):
    nome = models.CharField(max_length=200)
    ca = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
