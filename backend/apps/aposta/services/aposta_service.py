# listar_apostas
# listar_apostas (com id)
# Cadastrar_aposta
# editar_aposta (id)
# remover_aposta
from django.http.response import Http404
from ..models import Aposta
from apps.campeonato.services import rodada_service
#campeonato.services import rodada_service


def listar_apostas():
    return Aposta.objects.all()


def cadastrar_aposta(aposta_nova):
    return Aposta.objects.create(usuario=aposta_nova.usuario, rodada=aposta_nova.rodada )


def listar_aposta_id(id):
    try:
        return Aposta.objects.get(id=id)
    except Aposta.DoesNotExist:
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
            # Se existir aposta para a rodada
            if apostas_rodada:
                # adicionando na lista de retorno
                lista.append(apostas_rodada[0])
    else:
        return Http404
    
    return lista


def editar_aposta(aposta_antiga, aposta_nova):
    aposta_antiga.usuario = aposta_nova.usuario
    aposta_antiga.rodada = aposta_nova.rodada
    aposta_antiga.save(force_update=True)


def remover_aposta(aposta):
    aposta.delete()