from rest_framework.response import Response
from rest_framework.views import APIView
from ..services import rodada_service
from ..serializers import rodada_serializer
from rest_framework import status
from ..entidades import rodada

class RodadaList(APIView):
    def get(self, request, format=None):
        rodada = rodada_service.listar_rodada()
        serializer = rodada_serializer.RodadaSerializer(rodada, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 

    def post(self, request, format=None):
        serializer = rodada_serializer.RodadaSerializer(data=request.data)
        if serializer.is_valid():
            campeonato = serializer.validated_data["campeonato"]
            numero = serializer.validated_data["numero"]
            rodada_nova = rodada.Rodada(numero=numero, campeonato=campeonato)
            rodada_service.cadastrar_rodada(rodada_nova)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RodadaDetails(APIView):
    def get(self, request, id, format=None):
        rodada = rodada_service.listar_rodada_id(id)
        serializer = rodada_serializer.RodadaSerializer(rodada)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id, format=None):
        rodada_antiga = rodada_service.listar_rodada_id(id)
        serializer = rodada_serializer.RodadaSerializer(rodada_antiga, data=request.data)
        if serializer.is_valid():
            numero = serializer.validated_data["numero"]
            campeonato = serializer.validated_data["campeonato"]
            rodada_nova = rodada.Rodada(numero=numero, campeonato=campeonato)
            rodada_service.editar_rodada(rodada_antiga, rodada_nova)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        rodada = rodada_service.listar_rodada_id(id)
        rodada_service.remover_rodada(rodada)
        return Response(status=status.HTTP_204_NO_CONTENT)


    def patch(self, request, id, format=None):
        rodada = rodada_service.listar_rodada_id(id)
        serializer = rodada_serializer.RodadaSerializer(rodada, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(force_update=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RodadaCamp(APIView):
    def get(self, request, format=None):
        query_params = request.query_params
        campeonato = query_params.get('campeonato', None)
        if campeonato is None:
            errors = {
                'campeonato': "Campo Obrigatorio"
            }
            return Response(errors,status=status.HTTP_400_BAD_REQUEST)

        lista_rodada = rodada_service.listar_rodada_campeonato(campeonato)
        serializer = rodada_serializer.RodadaSerializer(lista_rodada, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
