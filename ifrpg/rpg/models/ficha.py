from django.db import models
from django.contrib.auth.models import User

class Ficha(models.Model):
    nome = models.CharField(max_length=100)
    jogador = models.ForeignKey(User, related_name='fichas', on_delete=models.CASCADE)
    rpg = models.ForeignKey('rpg.RPGmodel', related_name='fichas', on_delete=models.CASCADE)
    classe = models.CharField(max_length=100, blank=True)
    antecedente = models.CharField(max_length=100, blank=True)
    raça = models.CharField(max_length=100)
    alinhamento = models.CharField(max_length=100, blank=True)
    experiencia = models.IntegerField(default=0)

    inspiração = models.IntegerField(default=0)
    pontos_de_vida_maximos = models.IntegerField(default=0)
    dado_de_vida = models.CharField(max_length=20, default='0')

    força = models.IntegerField(default=0)
    destreza = models.IntegerField(default=0)
    constituição = models.IntegerField(default=0)
    inteligencia = models.IntegerField(default=0)
    sabedoria = models.IntegerField(default=0)
    carisma = models.IntegerField(default=0)

    def __str__(self):
        return self.nome