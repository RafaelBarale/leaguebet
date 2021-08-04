# listar_apostas
# listar_apostas (com id)
# Cadastrar_aposta
# editar_aposta (id)
# remover_aposta
from django.http.response import Http404
from ..models import ApostaJogo


def listar_apostajogo():
    return ApostaJogo.objects.all()


def cadastrar_apostajogo(apostajogo_nova):
    return ApostaJogo.objects.create(jogo=apostajogo_nova.jogo, aposta=apostajogo_nova.aposta, gol_casa=apostajogo_nova.gol_casa, gol_visitante=apostajogo_nova.gol_visitante)


def listar_apostajogo_id(id):
    try:
        return ApostaJogo.objects.get(id=id)
    except ApostaJogo.DoesNotExist:
        raise Http404


def listar_aposta_campeonato_rodada(usuario, campeonato, rodada):
    lista = []
    if usuario is not None and rodada is not None:
        lista = Aposta.objects.filter(usuario=usuario, rodada=rodada)
    elif campeonato is not None and usuario is not None:
        #listando todas as rodadas do campeonato
        rodadas_camp = rodada_service.listar_rodada_campeonato(campeonato=campeonato)
        for rodada in rodadas_camp:
            # Buscando as apostas para cada rodada 
            apostas_rodada = Aposta.objects.filter(rodada=rodada,usuario=usuario)
            # Se existir aposta para a rodada
            if apostas_rodada:
                # adicionando na lista de retorno
                lista.append(apostas_rodada[0])
    elif usuario is not None:
        lista = Aposta.objects.filter(usuario=usuario)
    elif rodada is not None:
        lista = Aposta.objects.filter(rodada=rodada)
    elif campeonato is not None:
        #listando todas as rodadas do campeonato
        rodadas_camp = rodada_service.listar_rodada_campeonato(campeonato=campeonato)
        for rodada in rodadas_camp:
            # Buscando as apostas para cada rodada 
            apostas_rodada = Aposta.objects.filter(rodada=rodada)
            for aposta in apostas_rodada:
                lista.append(aposta)

            # Se existir aposta para a rodada
            #if apostas_rodada:
                # adicionando na lista de retorno
            #    lista.append(apostas_rodada[0])
    else:
        return Http404
    
    return lista


def editar_apostajogo(apostajogo_antiga, apostajogo_nova):
    apostajogo_antiga.jogo = apostajogo_nova.jogo
    apostajogo_antiga.aposta = apostajogo_nova.aposta
    apostajogo_antiga.gol_casa = apostajogo_nova.gol_casa
    apostajogo_antiga.gol_visitante = apostajogo_nova.gol_visitante
    apostajogo_antiga.save(force_update=True)


def remover_apostajogo(apostajogo):
    apostajogo.delete()