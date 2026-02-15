from django.db import models
from django.contrib.auth.models import User

class Ataques(models.Model):
    ficha = models.ForeignKey('Ficha', on_delete=models.CASCADE)
    nome_ataque = models.CharField(max_length=100, blank=True, null=True)
    acerto_ataque = models.CharField(max_length=50, blank=True, null=True)
    dano_ataque = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Ataques"
    def __str__(self):
        return self.nome_ataque