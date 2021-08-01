from django.http.response import Http404
from ..models import Classificacao
#from backend.apps.clube.services.clube_service import listar_clube_id
from apps.clube.services import clube_service

def listar_classificacao():
    return Classificacao.objects.all()


def listar_clssificacao_campeonato(campeonato):
    try:
        #classificacoes = Classificacao.objects.filter(campeonato=campeonato)
        return Classificacao.objects.filter(campeonato=campeonato)
    except Classificacao.DoesNotExist:
        return Http404
    #return classificacoes


def cadastrar_classificacao(classificacao_nova):
    classificacao_db = Classificacao.objects.create(campeonato=classificacao_nova.campeonato)
    #return Classificacao.objects.create(campeonato=classificacao_nova.campeonato, clube=classificacao_nova.clube)
    classificacao_db.save()
    for i in classificacao_nova.clube:
        clube = clube_service.listar_clube_id(i.id)
        classificacao_db.clube.add(clube)
    return classificacao_db


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