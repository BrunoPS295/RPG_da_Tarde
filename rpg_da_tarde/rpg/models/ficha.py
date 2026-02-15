from django.db import models
from django.contrib.auth.models import User

class Ficha(models.Model):
    rpg = models.ForeignKey('rpg.RPGmodel', related_name='fichas', on_delete=models.CASCADE, blank=True, null=True)
    jogador = models.ForeignKey(User, related_name='fichas', on_delete=models.CASCADE)
    nome = models.CharField(max_length=100, blank=True, null=True)
    classe = models.CharField(max_length=100, blank=True, null=True)
    antecedente = models.CharField(max_length=100, blank=True, null=True)
    raca = models.CharField(max_length=100, blank=True, null=True)
    alinhamento = models.CharField(max_length=100, blank=True, null=True)
    experiencia = models.IntegerField(default=0, blank=True, null=True)

    inspiracao = models.IntegerField(default=0, blank=True, null=True)
    max_pv = models.IntegerField(default=0, blank=True, null=True)
    temp_pv = models.IntegerField(default=0, blank=True, null=True)
    atual_pv = models.IntegerField(default= None, blank=True, null=True)
    i_pv = models.IntegerField(default=0, blank=True, null=True)
    dado_de_vida = models.CharField(max_length=20, default='0', blank=True, null=True)
    bonus_de_proficiencia = models.IntegerField(default=0, blank=True, null=True)

    forca = models.IntegerField(default=0,blank=True, null=True)
    destreza = models.IntegerField(default=0,blank=True, null=True)
    constituicao = models.IntegerField(default=0,blank=True, null=True)
    inteligencia = models.IntegerField(default=0,blank=True, null=True)
    sabedoria = models.IntegerField(default=0,blank=True, null=True)
    carisma = models.IntegerField(default=0,blank=True, null=True)

    prof_check = models.JSONField(default=list, blank=True)

    morte = models.BooleanField(default=False)

    textao = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.atual_pv is None or self.atual_pv > self.max_pv + self.temp_pv or self.atual_pv <= 0:
            self.atual_pv = (self.max_pv or -1) + (self.temp_pv or -1)
        super().save(*args, **kwargs)

    def __str__(self):
        if self.nome != None and self.nome != "":
            return self.nome
        return f"Ficha de {self.jogador.username}"