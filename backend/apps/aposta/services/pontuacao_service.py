from django.http.response import Http404
from ..models import Pontuacao


def listar_pontuacao():
    return Pontuacao.objects.all()


def cadastrar_pontuacao(pontuacao_nova):
    return Pontuacao.objects.create(campeonato=pontuacao_nova.campeonato, usuario=pontuacao_nova.usuario, pontos=pontuacao_nova.pontos)


def listar_pontuacao_id(id):
    try:
        return Pontuacao.objects.get(id=id)
    except Pontuacao.DoesNotExist:
        raise Http404

def listar_pontuacao_campeonato(campeonato):
    try:
        return Pontuacao.objects.filter(campeonato=campeonato)
    except Pontuacao.DoesNotExist:
        raise Http404


def editar_pontuacao(pontuacao_antiga, pontuacao_nova):
    pontuacao_antiga.campeonato = pontuacao_nova.campeonato
    pontuacao_antiga.vencedor = pontuacao_nova.vencedor
    pontuacao_antiga.golCasa = pontuacao_nova.golCasa
    pontuacao_antiga.golVisitante = pontuacao_nova.golVisitante
    pontuacao_antiga.save(force_update=True)


def remover_pontuacao(pontuacao):
    pontuacao.delete()
