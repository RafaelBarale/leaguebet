from django.http.response import Http404
from ..models import Rodada


def listar_rodada():
    return Rodada.objects.all()


def cadastrar_rodada(rodada_nova):
    return Rodada.objects.create(numero=rodada_nova.numero, campeonato=rodada_nova.campeonato, fechada=rodada_nova.fechada)


def listar_rodada_id(id):
    try:
        return Rodada.objects.get(id=id)
    except Rodada.DoesNotExist:
        raise Http404


def listar_rodada_campeonato(campeonato):
    if campeonato is not None:
        return Rodada.objects.filter(campeonato=campeonato)
    else:
        return Http404


def editar_rodada(rodada_antiga, rodada_nova):
    rodada_antiga.numero = rodada_nova.numero
    rodada_antiga.campeonato = rodada_nova.campeonato
    rodada_antiga.fechada = rodada_nova.fechada
    rodada_antiga.save(force_update=True)


def remover_rodada(rodada):
    rodada.delete()