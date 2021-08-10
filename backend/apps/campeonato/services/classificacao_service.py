from django.http.response import Http404
from ..models import Classificacao
from ..entidades import classificacao

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


def atualiza_classificacao(campeonato, clube, golpro, golcontra):
    classificacao_nova = classificacao.Classificacao(campeonato=campeonato, clube=clube, pontos=0, jogos=0, vitorias=0, derrotas=0, empates=0, gols_contra=0, gols_pro=0)
    # buscando a classificacao antiga
    classificacoes = listar_classificacao_campeonato(campeonato, clube)
    if classificacoes:
        classificacao_atual = listar_classificacao_id(classificacoes[0].id)
    else:
        # criar classificacao para o clube
        classificacao_atual = cadastrar_classificacao(classificacao_nova)

    classificacao_nova.jogos = classificacao_atual.jogos + 1
    classificacao_nova.gols_pro = classificacao_atual.gols_pro + golpro
    classificacao_nova.gols_contra = classificacao_atual.gols_contra + golcontra
    if golpro == golcontra:
        classificacao_nova.pontos = classificacao_atual.pontos + 1
        classificacao_nova.empates = classificacao_atual.empates + 1
    elif golpro > golcontra:
        classificacao_nova.pontos = classificacao_atual.pontos + 3
        classificacao_nova.vitorias = classificacao_atual.vitorias = 1
    else:
        classificacao_nova.derrotas = classificacao_atual.derrotas = 1

    editar_classificacao(classificacao_atual,classificacao_nova)