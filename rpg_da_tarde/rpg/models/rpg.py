import secrets
from django.db import models
from django.contrib.auth.models import User

class RPGmodel(models.Model):
    rpg_nome = models.CharField(max_length=100)
    mestre = models.ForeignKey(User, related_name='mestre', on_delete=models.CASCADE)
    jogadores = models.ManyToManyField(User, related_name='jogadores')
    key = models.CharField(max_length=10, unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = secrets.token_urlsafe(7)
            while RPGmodel.objects.filter(key=self.key).exists():
                self.key = secrets.token_urlsafe(7)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.rpg_nome
    
    class Meta:
        verbose_name = "RPG"
        verbose_name_plural = "RPGS"
        
    def __str__(self):
        return self.rpg_nome