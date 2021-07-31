from rest_framework.response import Response
from rest_framework.views import APIView
from ..services import clube_service
from ..serializers import clube_serializer
from rest_framework import status
from ..entidades import clube

class ClubeList(APIView):
    def get(self, request, format=None):
        clubes = clube_service.listar_clubes()
        serializer = clube_serializer.ClubeSerializer(clubes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 

    def post(self, request, format=None):
        serializer = clube_serializer.ClubeSerializer(data=request.data)
        if serializer.is_valid():
            nome = serializer.validated_data["nome"]
            nome_abreviado = serializer.validated_data["nome_abreviado"]
            estado = serializer.validated_data["estado"]
            escudo = serializer.validated_data["escudo"]

            clube_novo = clube.Clube(nome=nome, nome_abreviado=nome_abreviado, estado=estado, escudo=escudo)
            clube_db = clube_service.cadastrar_clube(clube_novo)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClubeDetails(APIView):
    def get(self, request, id, format=None):
        clube = clube_service.listar_clube_id(id)
        serializer = clube_serializer.ClubeSerializer(clube)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id, format=None):
        clube_antigo = clube_service.listar_clube_id(id)
        serializer = clube_serializer.ClubeSerializer(clube_antigo, data=request.data)
        if serializer.is_valid():
            nome = serializer.validated_data["nome"]
            nome_abreviado = serializer.validated_data["nome_abreviado"]
            estado = serializer.validated_data["estado"]
            escudo = serializer.validated_data["escudo"]
            clube_novo = clube.Clube(nome=nome, nome_abreviado=nome_abreviado, estado=estado, escudo=escudo)
            clube_service.editar_clube(clube_antigo, clube_novo)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        clube = clube_service.listar_clube_id(id)
        clube_service.remover_clube(clube)
        return Response(status=status.HTTP_204_NO_CONTENT)
