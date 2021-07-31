from rest_framework.response import Response
from rest_framework.views import APIView
from ..services import campeonato_service
from ..serializers import campeonato_serializer
from rest_framework import status
from ..entidades import campeonato

class CampeonatoList(APIView):
    def get(self, request, format=None):
        campeonatos = campeonato_service.listar_campeonato()
        serializer = campeonato_serializer.CampeonatoSerializer(campeonatos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 

    def post(self, request, format=None):
        serializer = campeonato_serializer.CampeonatoSerializer(data=request.data)
        if serializer.is_valid():
            nome = serializer.validated_data["nome"]
            temporada = serializer.validated_data["temporada"]
            campeonato_novo = campeonato.Campeonato(nome=nome, temporada=temporada)
            campeonato_service.cadastrar_campeonato(campeonato_novo)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CampeonatoDetails(APIView):
    def get(self, request, id, format=None):
        campeonato = campeonato_service.listar_campeonato_id(id)
        serializer = campeonato_serializer.CampeonatoSerializer(campeonato)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id, format=None):
        campeonato_antigo = campeonato_service.listar_campeonato_id(id)
        serializer = campeonato_serializer.CampeonatoSerializer(campeonato_antigo, data=request.data)
        if serializer.is_valid():
            nome = serializer.validated_data["nome"]
            temporada = serializer.validated_data["temporada"]
            
            campeonato_novo = campeonato.Campeonato(nome=nome, temporada=temporada)
            campeonato_service.editar_campeonato(campeonato_antigo, campeonato_novo)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        campeonato = campeonato_service.listar_campeonato_id(id)
        campeonato_service.remover_campeonato(campeonato)
        return Response(status=status.HTTP_204_NO_CONTENT)
