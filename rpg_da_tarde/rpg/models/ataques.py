from django.db import models
from django.contrib.auth.models import User

class Ataques(models.Model):
    ficha = models.ForeignKey('Ficha', on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    acerto = models.CharField(max_length=50)
    dano = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Ataques"
    def __str__(self):
        return self.nome