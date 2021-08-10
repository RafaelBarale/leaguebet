from apps.campeonato.services import jogo_service
from django.http.response import Http404
from ..models import Pontuacao, Regra
from ..services import aposta_service
from ..entidades import pontuacao


def listar_pontuacao():
    return Pontuacao.objects.all()


def cadastrar_pontuacao(pontuacao_nova):
    return Pontuacao.objects.create(campeonato=pontuacao_nova.campeonato, usuario=pontuacao_nova.usuario, pontos=pontuacao_nova.pontos)


def listar_pontuacao_id(id):
    try:
        return Pontuacao.objects.get(id=id)
    except Pontuacao.DoesNotExist:
        raise Http404

def listar_pontuacao_campeonato(campeonato):
    try:
        return Pontuacao.objects.filter(campeonato=campeonato)
    except Pontuacao.DoesNotExist:
        raise Http404

def listar_pontuacao_campeonato_usuario(campeonato, usuario):
    try:
        return Pontuacao.objects.filter(campeonato=campeonato, usuario=usuario)
    except Pontuacao.DoesNotExist:
        raise Http404

def editar_pontuacao(pontuacao_antiga, pontuacao_nova):
    pontuacao_antiga.campeonato = pontuacao_nova.campeonato
    pontuacao_antiga.pontos = pontuacao_nova.pontos
    pontuacao_antiga.usuario = pontuacao_nova.usuario
    pontuacao_antiga.save(force_update=True)


def remover_pontuacao(pontuacao):
    pontuacao.delete()


def aplicar_pontuacao(jogo):
    pontos = 0
    # Buscando as regras de pontuação do campeonato
    try:
        regra_campeonato = Regra.objects.get(campeonato=jogo.campeonato)
        # buscando todas as apostas do jogo
        apostas_jogo = aposta_service.listar_aposta_jogo(jogo=jogo)
        # Para cada aposta, faço a pontuação conforme a regra e salvo
        for aposta in apostas_jogo:
            # Buscando a pontuação do usuario no campeonato
            pontuacao_atual = listar_pontuacao_campeonato_usuario(campeonato=jogo.campeonato, usuario=aposta.usuario)
            # Se exitir pontuação do usuario e campeonato, capturo os pontos,
            # caso contrario crio uma instancia para pontuação atual
            if pontuacao_atual:
                pontos = pontuacao_atual[0].pontos
                campeonato = pontuacao_atual[0].campeonato
                usuario = pontuacao_atual[0].usuario
                pontuacao_atual = listar_pontuacao_id(pontuacao_atual[0].id)
            else:
                campeonato = jogo.campeonato
                usuario = aposta.usuario
                pontos = 0
                nova = pontuacao.Pontuacao(campeonato=campeonato,usuario=usuario, pontos=pontos)
                pontuacao_atual = cadastrar_pontuacao(nova)
            
            if jogo.gols_casa == aposta.gol_casa:
                pontos += regra_campeonato.golCasa
            if jogo.gols_visitante == aposta.gol_visitante:
                pontos += regra_campeonato.golVisitante
            
            if ((jogo.gols_casa > jogo.gols_visitante and aposta.gol_casa > aposta.gol_visitante) 
                or (jogo.gols_casa < jogo.gols_visitante and aposta.gol_casa < aposta.gol_visitante)
                or (jogo.gols_casa == jogo.gols_visitante and aposta.gol_casa == aposta.gol_visitante)):
                pontos += regra_campeonato.vencedor

            # Criando uma nova instancia da pontuação
            pontuacao_nova = pontuacao.Pontuacao(campeonato=campeonato,usuario=usuario, pontos=pontos)
            editar_pontuacao(pontuacao_antiga=pontuacao_atual, pontuacao_nova=pontuacao_nova)    

    except Regra.DoesNotExist:
        raise Http404
    

            

