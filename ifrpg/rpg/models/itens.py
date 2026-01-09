from django.db import models
from django.contrib.auth.models import User

class Itens(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    class Meta:
        verbose_name_plural = "Itens"

    def __str__(self):
        return self.nome