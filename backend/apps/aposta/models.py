from django.db.models.deletion import PROTECT
from django.db import models
from django.contrib.auth.models import User
from apps.campeonato.models import Jogo, Campeonato


class Aposta(models.Model):
    gol_casa = models.IntegerField(null=False, blank=False)
    gol_visitante = models.IntegerField(null=False, blank=False)
    jogo = models.ForeignKey(Jogo, on_delete=models.PROTECT)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.jogo)

    class Meta:
        unique_together = ('usuario', 'jogo',)


class Regra(models.Model):
    campeonato = models.ForeignKey(Campeonato, on_delete=PROTECT)
    vencedor = models.IntegerField(null=False, blank=False)
    golCasa = models.IntegerField(null=False, blank=False)
    golVisitante = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return str(self.campeonato)

    class Meta:
        unique_together = ('campeonato',)

