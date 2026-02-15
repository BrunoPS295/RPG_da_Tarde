from django.db import models
from django.contrib.auth.models import User

class Ataques(models.Model):
    ficha = models.ForeignKey('Ficha', on_delete=models.CASCADE)
    nome_ataque = models.CharField(max_length=100)
    acerto_ataque = models.CharField(max_length=50)
    dano_ataque = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Ataques"
    def __str__(self):
        return self.nome_ataque