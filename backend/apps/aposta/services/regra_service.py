from django.http.response import Http404
from ..models import Regra


def listar_regra():
    return Regra.objects.all()


def cadastrar_regra(regra_nova):
    return Regra.objects.create(campeonato=regra_nova.campeonato, vencedor=regra_nova.vencedor, golCasa=regra_nova.golCasa, golVisitante=regra_nova.golVisitante)


def listar_regra_id(id):
    try:
        return Regra.objects.get(id=id)
    except Regra.DoesNotExist:
        raise Http404

def listar_regra_campeonato(campeonato):
    try:
        return Regra.objects.filter(campeonato=campeonato)
    except Regra.DoesNotExist:
        raise Http404


def editar_regra(regra_antiga, regra_nova):
    regra_antiga.campeonato = regra_nova.campeonato
    regra_antiga.vencedor = regra_nova.vencedor
    regra_antiga.golCasa = regra_nova.golCasa
    regra_antiga.golVisitante = regra_nova.golVisitante
    regra_antiga.save(force_update=True)


def remover_regra(regra):
    regra.delete()
