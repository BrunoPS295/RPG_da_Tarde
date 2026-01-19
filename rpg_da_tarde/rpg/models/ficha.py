from django.db import models
from django.contrib.auth.models import User

class Ficha(models.Model):
    rpg = models.ForeignKey('rpg.RPGmodel', related_name='fichas', on_delete=models.CASCADE, blank=True, null=True)
    jogador = models.ForeignKey(User, related_name='fichas', on_delete=models.CASCADE)
    nome = models.CharField(max_length=100,blank=True, null=True)
    classe = models.CharField(max_length=100, blank=True, null=True)
    antecedente = models.CharField(max_length=100, blank=True, null=True)
    raca = models.CharField(max_length=100, blank=True, null=True)
    alinhamento = models.CharField(max_length=100, blank=True, null=True)
    experiencia = models.IntegerField(default=0)

    inspiracao = models.IntegerField(default=0)
    max_pv = models.IntegerField(default=0)
    dado_de_vida = models.CharField(max_length=20, default='0')
    bonus_de_proficiencia = models.IntegerField(default=0)

    forca = models.IntegerField(default=0,blank=True, null=True)
    destreza = models.IntegerField(default=0,blank=True, null=True)
    constituicao = models.IntegerField(default=0,blank=True, null=True)
    inteligencia = models.IntegerField(default=0,blank=True, null=True)
    sabedoria = models.IntegerField(default=0,blank=True, null=True)
    carisma = models.IntegerField(default=0,blank=True, null=True)

    prof_check = models.JSONField(default=list, blank=True)

    def __str__(self):
        return self.nome