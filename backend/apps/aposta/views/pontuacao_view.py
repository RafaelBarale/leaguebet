from apps.campeonato.services import campeonato_service
from rest_framework.response import Response
from rest_framework.views import APIView
from ..services import pontuacao_service
from ..serializers import pontuacao_serializer
from rest_framework import status
from ..entidades import pontuacao


class PontuacaoList(APIView):
    def get(self, request, format=None):
        pontuacao = pontuacao_service.listar_pontuacao()
        serializer = pontuacao_serializer.PontuacaoSerializer(pontuacao, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 
'''
#DEVE-SE CRIAR PONTUAÇÃO APENAS QUANDO ATUALIZAR OS JOGOS

    def post(self, request, format=None):
        serializer = pontuacao_serializer.PontuacaoSerializer(data=request.data)
        if serializer.is_valid():
            campeonato = serializer.validated_data["campeonato"]
            usuario = serializer.validated_data['usuario']
            pontos = serializer.validated_data["pontos"]
            pontuacao_nova = pontuacao.Pontuacao(campeonato=campeonato,usuario=usuario, pontos=pontos)
            pontuacao_service.cadastrar_pontuacao(pontuacao_nova)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''

class PontuacaoDetails(APIView):
    def get(self, request, id, format=None):
        pontuacao = pontuacao_service.listar_pontuacao_id(id)
        serializer = pontuacao_serializer.PontuacaoSerializer(pontuacao)
        return Response(serializer.data, status=status.HTTP_200_OK)

#MANIPULAR PONTUAÇÃO APENAS QUANDO ATUALIZAR OS JOGOS - recursos no backend

    def put(self, request, id, format=None):
        pontuacao_antiga = pontuacao_service.listar_pontuacao_id(id)
        serializer = pontuacao_serializer.PontuacaoSerializer(pontuacao_antiga, data=request.data)
        if serializer.is_valid():
            campeonato = serializer.validated_data["campeonato"]
            usuario = serializer.validated_data['usuario']
            pontos = serializer.validated_data["pontos"]
            pontuacao_nova = pontuacao.Pontuacao(campeonato=campeonato,usuario=usuario, pontos=pontos)
            pontuacao_service.editar_pontuacao(pontuacao_antiga, pontuacao_nova)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        pontuacao = pontuacao_service.listar_pontuacao_id(id)
        pontuacao_service.remover_pontuacao(pontuacao)
        return Response(status=status.HTTP_204_NO_CONTENT)


    def patch(self, request, id, format=None):
        pontuacao = pontuacao_service.listar_pontuacao_id(id)
        serializer = pontuacao_serializer.PontuacaoSerializer(pontuacao, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(force_update=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PontuacaoClass(APIView):
    def get(self, request, idcamp, format=None):
        campeonato = campeonato_service.listar_campeonato_id(idcamp)
        pontuacao = pontuacao_service.listar_pontuacao_campeonato(campeonato)
        serializer = pontuacao_serializer.PontuacaoSerializer(pontuacao, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)