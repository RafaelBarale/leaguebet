from django.http.response import Http404
from ..models import Classificacao

def listar_classificacao():
    return Classificacao.objects.all()


def listar_classificacao_campeonato(campeonato, clube):
    if clube is not None and campeonato is not None:
        return Classificacao.objects.filter(campeonato=campeonato, clube=clube)
    elif clube is None and campeonato is not None:
        return Classificacao.objects.filter(campeonato=campeonato)
    elif clube is not None and campeonato is None:
        return Classificacao.objects.filter(clube=clube)
    else:
        return Http404


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