from django.db import models
from django.contrib.auth.models import User

class Habilidades(models.Model):
    ficha = models.ForeignKey('Ficha', on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    duracao = models.IntegerField()
    buff = models.ForeignKey('Buff', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Habilidades"

    def __str__(self):
        return self.nome