from django.db import models
from django.contrib.auth.models import User

class Ficha(models.Model):
    rpg = models.ForeignKey('rpg.RPGmodel', related_name='fichas', on_delete=models.CASCADE)
    jogador = models.ForeignKey(User, related_name='fichas', on_delete=models.CASCADE)
    nome = models.CharField(max_length=100,blank=True, null=True)
    classe = models.CharField(max_length=100, blank=True, null=True)
    antecedente = models.CharField(max_length=100, blank=True, null=True)
    raca = models.CharField(max_length=100, blank=True, null=True)
    alinhamento = models.CharField(max_length=100, blank=True, null=True)
    experiencia = models.IntegerField(default=0)

    inspiracao = models.IntegerField(default=0)
    pontos_de_vida_maximos = models.IntegerField(default=0)
    dado_de_vida = models.CharField(max_length=20, default='0')

    forca = models.IntegerField(default=0)
    destreza = models.IntegerField(default=0)
    constituicao = models.IntegerField(default=0)
    inteligencia = models.IntegerField(default=0)
    sabedoria = models.IntegerField(default=0)
    carisma = models.IntegerField(default=0)

    def __str__(self):
        return self.nome