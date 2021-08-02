# listar_clube
# listar_clube (com id)
# Cadastrar_clube
# editar_clube (id)
# remover_clube
from django.http import Http404
from ..models import Clube
import os


def listar_clubes():
    clubes = Clube.objects.all()
    return clubes

def cadastrar_clube(clube):
    return Clube.objects.create(nome=clube.nome,nome_abreviado=clube.nome_abreviado,estado=clube.estado,escudo=clube.escudo)

def listar_clube_id(id):
    try:
        return Clube.objects.get(id=id)
    except Clube.DoesNotExist:
        raise Http404

def editar_clube(clube_antigo, clube_novo):
    clube_antigo.nome = clube_novo.nome
    clube_antigo.nome_abreviado = clube_novo.nome_abreviado
    clube_antigo.estado = clube_novo.estado
    clube_antigo.escudo = clube_novo.escudo
    clube_antigo.save(force_update=True)

def remover_clube(clube):
    #Apagando o escudo
    clube.escudo.delete()

    clube.delete()
