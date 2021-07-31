from django.db import models
from django.contrib.auth.models import User
from apps.campeonato.models import Campeonato, Rodada, Jogo 


class Aposta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    campeonato = models.ForeignKey(Campeonato, on_delete=models.PROTECT)
    rodada = models.ForeignKey(Rodada, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.usuario) + ' ' + str(self.rodada)

    class Meta:
        unique_together = ('usuario', 'campeonato', 'rodada',)


class ApostaJogo(models.Model):
    gol_casa = models.IntegerField(null=False, blank=False)
    gol_visitante = models.IntegerField(null=False, blank=False)
    aposta = models.ForeignKey(Aposta, on_delete=models.PROTECT)
    jogo = models.ForeignKey(Jogo, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.jogo)

    class Meta:
        unique_together = ('aposta', 'jogo',)
