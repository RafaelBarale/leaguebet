from django.http.response import Http404
from ..models import Classificacao


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
    return Classificacao.objects.create(campeonato=classificacao_nova.campeonato, clube=classificacao_nova.clube)


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