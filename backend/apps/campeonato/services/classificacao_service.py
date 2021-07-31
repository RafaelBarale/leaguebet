from django.http.response import Http404
from ..models import Classificacao


def listar_classificacao():
    return Classificacao.objects.all()


def cadastrar_campeonato(campeonato_novo):
    return Classificacao.objects.create(nome=campeonato_novo.nome, temporada=campeonato_novo.temporada)


def listar_classificacao_id(id):
    try:
        return Classificacao.objects.get(id=id)
    except Classificacao.DoesNotExist:
        raise Http404


def editar_classificacao(campeonato_antigo, campeonato_novo):
    campeonato_antigo.nome = campeonato_novo.nome
    campeonato_antigo.temporada = campeonato_novo.temporada
    campeonato_antigo.save(force_update=True)


def remover_classificacao(campeonato):
    campeonato.delete()