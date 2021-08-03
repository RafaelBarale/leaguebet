# listar_apostas
# listar_apostas (com id)
# Cadastrar_aposta
# editar_aposta (id)
# remover_aposta
from backend.apps.campeonato.models import Rodada
from django.http.response import Http404
from ..models import Aposta


def listar_apostas():
    return Aposta.objects.all()


def cadastrar_aposta(aposta_nova):
    return Aposta.objects.create(usuario=aposta_nova.usuario, campeonato=aposta_nova.campeonato, rodada=aposta_nova.rodada )


def listar_aposta_id(id):
    try:
        return Aposta.objects.get(id=id)
    except Aposta.DoesNotExist:
        raise Http404


def listar_aposta_campeonato_rodada(usuario, campeonato, rodada):
    lista = ''
    if campeonato is not None and rodada is not None and usuario is not None:
        lista = Aposta.objects.filter(usuario=usuario, campeonato=campeonato, rodada=rodada)
    elif campeonato is not None and usuario is not None:
        lista = Aposta.objects.filter(campeonato=campeonato, usuario=usuario)
    elif campeonato is not None and rodada is not None:
        lista = Aposta.objects.filter(campeonato=campeonato, rodada=rodada)
    elif campeonato is not None:
        lista = Aposta.objects.filter(campeonato=campeonato)
    else:
        return Http404
    
    return lista


def editar_aposta(aposta_antiga, aposta_nova):
    aposta_antiga.usuario = aposta_nova.usuario
    aposta_antiga.rodada = aposta_nova.rodada
    aposta_antiga.campeonato = aposta_nova.campeonato
    aposta_antiga.save(force_update=True)


def remover_aposta(aposta):
    aposta.delete()