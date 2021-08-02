from rest_framework.response import Response
from rest_framework.views import APIView
from ..services import jogo_service
from ..serializers import jogo_serializer
from rest_framework import status
from ..entidades import jogo

class JogoList(APIView):
    def get(self, request, format=None):
        jogos = jogo_service.listar_jogo()
        serializer = jogo_serializer.JogoSerializer(jogos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 

    def post(self, request, format=None):
        serializer = jogo_serializer.JogoSerializer(data=request.data)
        if serializer.is_valid():
            gols_casa = serializer.validated_data["gols_casa"]
            gols_visitante = serializer.validated_data["gols_visitante"]
            clube_casa = serializer.validated_data["clube_casa"]
            clube_visitante = serializer.validated_data["clube_visitante"]
            campeonato = serializer.validated_data["campeonato"]
            rodada = serializer.validated_data["rodada"]
            jogo_novo = jogo.Jogo(gols_casa=gols_casa, gols_visitante=gols_visitante, clube_casa=clube_casa, clube_visitante=clube_visitante,
                                 campeonato=campeonato, rodada=rodada)
            jogo_service.cadastrar_jogo(jogo_novo)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JogoDetails(APIView):
    def get(self, request, id, format=None):
        jogo = jogo_service.listar_jogo_id(id)
        serializer = jogo_serializer.JogoSerializer(jogo)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id, format=None):
        jogo_antigo = jogo_service.listar_jogo_id(id)
        serializer = jogo_serializer.JogoSerializer(jogo_antigo, data=request.data)
        if serializer.is_valid():
            gols_casa = serializer.validated_data["gols_casa"]
            gols_visitante = serializer.validated_data["gols_visitante"]
            clube_casa = serializer.validated_data["clube_casa"]
            clube_visitante = serializer.validated_data["clube_visitante"]
            campeonato = serializer.validated_data["campeonato"]
            rodada = serializer.validated_data["rodada"]
            
            jogo_novo = jogo.Jogo(gols_casa=gols_casa, gols_visitante=gols_visitante, clube_casa=clube_casa, clube_visitante=clube_visitante,
                                    campeonato=campeonato, rodada=rodada)
            jogo_service.editar_jogo(jogo_antigo, jogo_novo)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        jogo = jogo_service.listar_jogo_id(id)
        jogo_service.remover_jogo(jogo)
        return Response(status=status.HTTP_204_NO_CONTENT)


    def patch(self, request, id, format=None):
        jogo = jogo_service.listar_jogo_id(id)
        clube_casa = request.data.get('clube_casa', None)
        clube_visitante = request.data.get('clube_visitante', None)
        
        if clube_casa is None:
            clube_casa = jogo.clube_casa_id
            request.data.update({"clube_casa": clube_casa})
        
        if clube_visitante is None:
            clube_visitante = jogo.clube_visitante_id
            request.data.update({"clube_visitante": clube_visitante})
        serializer = jogo_serializer.JogoSerializer(jogo, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save(force_update=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JogoRodadaCamp(APIView):
    def get(self, request, format=None):
        query_params = request.query_params
        campeonato = query_params.get('campeonato', None)
        rodada = query_params.get('rodada', None)
        if campeonato is None and rodada is None:
            errors = {
                "campeonato": "Campo obrigatorio",
                "clube": "Campo obrigatorio"
            }
            return Response(errors,status=status.HTTP_400_BAD_REQUEST)
        lista_jogos = jogo_service.listar_jogo_campeonato_rodada(campeonato=campeonato, rodada=rodada)
        serializer = jogo_serializer.JogoSerializer(lista_jogos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
