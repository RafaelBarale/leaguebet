from rest_framework.response import Response
from rest_framework.views import APIView
from ..services import classificacao_service
from ..serializers import classificacao_serializer
from rest_framework import status
from ..entidades import classificacao

class ClassificacaoList(APIView):
    def get(self, request, format=None):
        classificacoes = classificacao_service.listar_classificacao()
        serializer = classificacao_serializer.ClassificacaoSerializer(classificacoes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 

    def post(self, request, format=None):
        serializer = classificacao_serializer.ClassificacaoSerializer(data=request.data)
        if serializer.is_valid():
            campeonato = serializer.validated_data["campeonato"]
            clube = serializer.validated_data["clube"]
            classificacao_nova = classificacao.Classificacao(campeonato=campeonato, clube=clube)
            classificacao_service.cadastrar_classificacao(classificacao_nova)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClassificacaoDetails(APIView):
    def get(self, request, id, format=None):
        classificacao = classificacao_service.listar_classificacao_id(id)
        serializer = classificacao_serializer.ClassificacaoSerializer(classificacao)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id, format=None):
        classificacao_antiga = classificacao_service.listar_classificacao_id(id)
        serializer = classificacao_serializer.ClassificacaoSerializer(classificacao_antiga, data=request.data)
        if serializer.is_valid():
            pontos = serializer.validated_data["pontos"]
            jogos = serializer.validated_data["jogos"]
            vitorias = serializer.validated_data["vitorias"]
            derrotas = serializer.validated_data["derrotas"]
            empates = serializer.validated_data["empates"]
            gols_pro = serializer.validated_data["gols_pro"]
            gols_contra = serializer.validated_data["gols_contra"]
            campeonato = serializer.validated_data["campeonato"]
            clube = serializer.validated_data["clube"]
            
            classificacao_nova = classificacao.Classificacao(pontos=pontos, jogos=jogos, vitorias=vitorias, derrotas=derrotas,
                                empates=empates, gols_pro=gols_pro, gols_contra=gols_contra, campeonato=campeonato, clube=clube)
            classificacao_service.editar_classificacao(classificacao_antiga, classificacao_nova)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        classificacao = classificacao_service.listar_classificacao_id(id)
        classificacao_service.remover_classificacao(classificacao)
        return Response(status=status.HTTP_204_NO_CONTENT)


    def patch(self, request, id, format=None):
        classificacao = classificacao_service.listar_classificacao_id(id)
        serializer = classificacao_serializer.ClassificacaoSerializer(classificacao, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(force_update=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClassifCamp(APIView):
    def get(self, request, format=None):
        query_params = request.query_params
        campeonato = query_params.get('campeonato', None)
        clube = query_params.get('clube', None)
        if campeonato is None and clube is None:
            errors = {
                "campeonato": "Campo obrigatorio",
                "clube": "Campo obrigatorio"
            }
            return Response(errors,status=status.HTTP_400_BAD_REQUEST)

        lista_classificacao = classificacao_service.listar_classificacao_campeonato(campeonato, clube)
        serializer = classificacao_serializer.ClassificacaoSerializer(lista_classificacao, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
