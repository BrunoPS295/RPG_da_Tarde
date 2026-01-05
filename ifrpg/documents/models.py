from django.db import models

class Documentos(models.Model):
    titulo = models.CharField(max_length=200)
    link = models.URLField(max_length=200, default="#")
    player = models.ForeignKey("face.Login", verbose_name=("player"), on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Documentos"

    def __str__(self):
        return self.titulo