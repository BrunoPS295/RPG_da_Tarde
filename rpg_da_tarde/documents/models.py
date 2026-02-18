from django.db import models
from django.contrib.auth.models import User

class Documentos(models.Model):
    titulo = models.CharField(max_length=200)
    arquivo = models.FileField(upload_to='documentos/documents', blank=True)
    usuario = models.ForeignKey(User, verbose_name=("usuario"), on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    permitidos = models.ManyToManyField(User, related_name='usuarios_permitidos', blank=True)

    class Meta:
        verbose_name_plural = "Documentos"

    def __str__(self):
        return self.titulo