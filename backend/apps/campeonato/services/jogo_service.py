from django.http.response import Http404
from ..models import Jogo


def listar_jogo():
    return Jogo.objects.all()


def cadastrar_jogo(jogo_novo):
    return Jogo.objects.create(gols_casa=jogo_novo.gols_casa, gols_visitante=jogo_novo.gols_visitante, clube_casa=jogo_novo.clube_casa, 
                                clube_visitante=jogo_novo.clube_visitante, rodada=jogo_novo.rodada, campeonato=jogo_novo.campeonato)


def listar_jogo_id(id):
    try:
        return Jogo.objects.get(id=id)
    except Jogo.DoesNotExist:
        raise Http404


def listar_jogo_campeonato_rodada(campeonato, rodada):
    if campeonato is not None and rodada is not None:
        return Jogo.objects.filter(campeonato=campeonato, rodada=rodada)
    elif campeonato is not None:
        return Jogo.objects.filter(campeonato=campeonato)
    elif rodada is not None:
        return Jogo.objects.filter(rodada=rodada)
    else:
        return Http404


def editar_jogo(jogo_antigo, jogo_novo):
    jogo_antigo.gols_casa = jogo_novo.gols_casa
    jogo_antigo.gols_visitante = jogo_novo.gols_visitante
    jogo_antigo.clube_casa = jogo_novo.clube_casa
    jogo_antigo.clube_visitante = jogo_novo.clube_visitante
    jogo_antigo.rodada = jogo_novo.rodada
    jogo_antigo.campeonato = jogo_novo.campeonato
    jogo_antigo.save(force_update=True)


def remover_jogo(jogo):
    jogo.delete()