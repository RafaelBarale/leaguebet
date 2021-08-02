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


def editar_classificacao(classificacao_antiga, classificacao_nova):
    classificacao_antiga.pontos = classificacao_nova.pontos
    classificacao_antiga.jogos = classificacao_nova.jogos
    classificacao_antiga.vitorias = classificacao_nova.vitorias
    classificacao_antiga.derrotas = classificacao_nova.derrotas
    classificacao_antiga.empates = classificacao_nova.empates
    classificacao_antiga.gols_pro = classificacao_nova.gols_pro
    classificacao_antiga.gols_contra = classificacao_nova.gols_contra
    classificacao_antiga.campeonato = classificacao_nova.campeonato
    classificacao_antiga.clube = classificacao_nova.clube
    classificacao_antiga.save(force_update=True)


def remover_classificacao(campeonato):
    campeonato.delete()