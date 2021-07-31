from django.db import models
from apps.clube.models import Clube


class Campeonato(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    temporada = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.nome


class Classificacao(models.Model):
    pontos = models.IntegerField(null=False, blank=False)
    jogos = models.IntegerField(null=False, blank=False)
    vitorias = models.IntegerField(null=False, blank=False)
    derrotas = models.IntegerField(null=False, blank=False)
    empates = models.IntegerField(null=False, blank=False)
    gols_pro = models.IntegerField(null=False, blank=False)
    gols_contra = models.IntegerField(null=False, blank=False)
    campeonato = models.ForeignKey(Campeonato, on_delete=models.PROTECT)
    clube = models.ManyToManyField(Clube)

    def __str__(self):
        return self.campeonato


class Rodada(models.Model):
    numero = models.IntegerField(null=False, blank=False)
    campeonato = models.ForeignKey(Campeonato, on_delete=models.PROTECT, null=False)

    def __str__(self):
        return str(self.campeonato) + ' ' + str(self.numero) + 'º Rodada'


class Jogo(models.Model):
    gols_casa = models.IntegerField(null=True, blank=True)
    gols_visitante = models.IntegerField(null=True, blank=True)
    clube_casa = models.ForeignKey(Clube, related_name='clube_casa', on_delete=models.PROTECT)
    clube_visitante = models.ForeignKey(Clube, related_name='clube_visitante', on_delete=models.PROTECT)
    rodada = models.ForeignKey(Rodada, on_delete=models.PROTECT)
    campeonato = models.ForeignKey(Campeonato, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.clube_casa) + ' X ' + str(self.clube_visitante)

    class Meta:
        unique_together = ('campeonato', 'clube_casa', 'clube_visitante',)
