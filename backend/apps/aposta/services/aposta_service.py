# listar_apostas
# listar_apostas (com id)
# Cadastrar_aposta
# editar_aposta (id)
# remover_aposta
from django.http.response import Http404
from ..models import Aposta
from apps.campeonato.services import jogo_service


def listar_apostageral():
    return Aposta.objects.all()


def cadastrar_aposta(aposta_nova):
    return Aposta.objects.create(jogo=aposta_nova.jogo, usuario=aposta_nova.usuario, gol_casa=aposta_nova.gol_casa, gol_visitante=aposta_nova.gol_visitante)


def listar_aposta_id(id):
    try:
        return Aposta.objects.get(id=id)
    except Aposta.DoesNotExist:
        raise Http404

def listar_aposta_jogo(jogo):
    try:
        return Aposta.objects.filter(jogo=jogo)
    except Aposta.DoesNotExist:
        raise Http404

def listar_aposta_usuario(usuario):
    try:
        return Aposta.objects.filter(usuario=usuario)
    except Aposta.DoesNotExist:
        raise Http404


def listar_aposta(usuario, jogo):
    lista = []
    if usuario is not None and jogo is not None:
        lista = Aposta.objects.filter(usuario=usuario, jogo=jogo)
    elif usuario is not None:
        lista = listar_aposta_usuario(usuario=usuario)
    elif jogo is not None:
        lista = listar_aposta_jogo(jogo=jogo)
    else:
        return Http404
    
    return lista


def listar_aposta_rodada(rodada, usuario):
    lista = []
    #Primeiro Listo todos os jogos da rodada
    jogos_rodada = jogo_service.listar_jogo_campeonato_rodada(rodada=rodada, campeonato=None)
    # Percorrendo os jogos da rodada, para buscar quais tem apostas vinculado
    for jogo in jogos_rodada:
        apostas = listar_aposta(jogo=jogo, usuario=usuario)
        for aposta in apostas:
            lista.append(aposta)

    return lista


def editar_aposta(aposta_antiga, aposta_nova):
    aposta_antiga.jogo = aposta_nova.jogo
    aposta_antiga.usuario = aposta_nova.usuario
    aposta_antiga.gol_casa = aposta_nova.gol_casa
    aposta_antiga.gol_visitante = aposta_nova.gol_visitante
    aposta_antiga.save(force_update=True)


def remover_aposta(aposta):
    aposta.delete()

