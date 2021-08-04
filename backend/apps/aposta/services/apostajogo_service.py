# listar_apostas
# listar_apostas (com id)
# Cadastrar_aposta
# editar_aposta (id)
# remover_aposta
from django.http.response import Http404
from ..models import ApostaJogo
from apps.campeonato.services import rodada_service, jogo_service


def listar_apostajogo():
    return ApostaJogo.objects.all()


def cadastrar_apostajogo(apostajogo_nova):
    return ApostaJogo.objects.create(jogo=apostajogo_nova.jogo, usuario=apostajogo_nova.usuario, gol_casa=apostajogo_nova.gol_casa, gol_visitante=apostajogo_nova.gol_visitante)


def listar_apostajogo_id(id):
    try:
        return ApostaJogo.objects.get(id=id)
    except ApostaJogo.DoesNotExist:
        raise Http404

def listar_apostajogo_jogo(jogo):
    try:
        return ApostaJogo.objects.filter(jogo=jogo)
    except ApostaJogo.DoesNotExist:
        raise Http404

def listar_apostajogo_usuario(usuario):
    try:
        return ApostaJogo.objects.filter(usuario=usuario)
    except ApostaJogo.DoesNotExist:
        raise Http404


def listar_apostajogo(usuario, jogo):
    lista = []
    if usuario is not None and jogo is not None:
        lista = ApostaJogo.objects.filter(usuario=usuario, jogo=jogo)
    elif usuario is not None:
        lista = listar_apostajogo_usuario(usuario=usuario)
    elif jogo is not None:
        lista = listar_apostajogo_jogo(jogo=jogo)
    else:
        return Http404
    
    return lista

def listar_apostajogo_rodada(rodada, usuario):
    lista = []
    #Primeiro Listo todos os jogos da rodada
    jogos_rodada = jogo_service.listar_jogo_campeonato_rodada(rodada=rodada)
    # Percorrendo os jogos da rodada, para buscar quais tem apostas vinculado
    for jogo in jogos_rodada:
        lista.append(listar_apostajogo(jogo=jogo, usuario=usuario))

    if lista:
        return lista
    else:
        return Http404


def editar_apostajogo(apostajogo_antiga, apostajogo_nova):
    apostajogo_antiga.jogo = apostajogo_nova.jogo
    apostajogo_antiga.usuario = apostajogo_nova.usuario
    apostajogo_antiga.gol_casa = apostajogo_nova.gol_casa
    apostajogo_antiga.gol_visitante = apostajogo_nova.gol_visitante
    apostajogo_antiga.save(force_update=True)


def remover_apostajogo(apostajogo):
    apostajogo.delete()