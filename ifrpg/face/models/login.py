from django.db import models

class Login(models.Model):
    player_nome = models.CharField(max_length=150, unique=True, verbose_name="Nome")
    senha = models.CharField(max_length=128)
    player_id = models.AutoField(primary_key=True)
    login_data = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Logins"

    def __str__(self):
        return self.player_nome