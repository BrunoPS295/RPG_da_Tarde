from django.db import models
from django.contrib.auth.models import User

class RPGmodel(models.Model):
    rpg_nome = models.CharField(max_length=100)
    mestre = models.ForeignKey(User, related_name='mestre', on_delete=models.CASCADE)
    jogadores = models.ManyToManyField(User, related_name='jogadores')

    class Meta:
        verbose_name = "RPG"
        verbose_name_plural = "RPGS"

    def __str__(self):
        return self.rpg_nome