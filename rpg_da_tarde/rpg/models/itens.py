from django.db import models
from django.contrib.auth.models import User

class Itens(models.Model):
    rpg_item = models.ForeignKey('RPGmodel', on_delete=models.CASCADE)
    ficha = models.ForeignKey('Ficha', on_delete=models.CASCADE)
    nome = models.CharField(max_length=100, blank=True, null=True)
    documento = models.FileField(upload_to='documentos/itens', blank=True, null=True)
    quantidade = models.IntegerField(default=1)
    equipado = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Itens"

    def __str__(self):
        if self.nome:
            return self.nome
        return f"Item {self.id}"