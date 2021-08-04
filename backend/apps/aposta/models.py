from django.db import models
from django.contrib.auth.models import User
from apps.campeonato.models import Jogo 


class ApostaJogo(models.Model):
    gol_casa = models.IntegerField(null=False, blank=False)
    gol_visitante = models.IntegerField(null=False, blank=False)
    jogo = models.ForeignKey(Jogo, on_delete=models.PROTECT)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.jogo)

    class Meta:
        unique_together = ('usuario', 'jogo',)
