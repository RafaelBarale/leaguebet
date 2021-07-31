from apps.campeonato.entidades import campeonato
from django.http.response import Http404
from ..models import Campeonato


def listar_campeonato():
    return Campeonato.objects.all()


def cadastrar_campeonato(campeonato_novo):
    return Campeonato.objects.create(nome=campeonato_novo.nome, temporada=campeonato_novo.temporada)


def listar_campeonato_id(id):
    try:
        return Campeonato.objects.get(id=id)
    except Campeonato.DoesNotExist:
        raise Http404


def editar_campeonato(campeonato_antigo, campeonato_novo):
    campeonato_antigo.nome = campeonato_novo.nome
    campeonato_antigo.temporada = campeonato_novo.temporada
    campeonato_antigo.save(force_update=True)


def remover_campeonato(campeonato):
    campeonato.delete()