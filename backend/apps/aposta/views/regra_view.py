from rest_framework.response import Response
from rest_framework.views import APIView
from ..services import regra_service
from ..serializers import regra_serializer
from rest_framework import status
from ..entidades import regra


class RegraList(APIView):
    def get(self, request, format=None):
        regra = regra_service.listar_regra()
        serializer = regra_serializer.RegraSerializer(regra, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 

    def post(self, request, format=None):
        serializer = regra_serializer.RegraSerializer(data=request.data)
        if serializer.is_valid():
            campeonato = serializer.validated_data["campeonato"]
            vencedor = serializer.validated_data['vencedor']
            golCasa = serializer.validated_data["golCasa"]
            golVisitante = serializer.validated_data['golVisitante']
            regra_nova = regra.Regra(campeonato=campeonato,vencedor=vencedor, golCasa=golCasa, golVisitante=golVisitante)
            regra_service.cadastrar_regra(regra_nova)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegraDetails(APIView):
    def get(self, request, id, format=None):
        regra = regra_service.listar_regra_id(id)
        serializer = regra_serializer.RegraSerializer(regra)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id, format=None):
        regra_antiga = regra_service.listar_regra_id(id)
        serializer = regra_serializer.RegraSerializer(regra_antiga, data=request.data)
        if serializer.is_valid():
            campeonato = serializer.validated_data["campeonato"]
            vencedor = serializer.validated_data['vencedor']
            golCasa = serializer.validated_data["golCasa"]
            golVisitante = serializer.validated_data['golVisitante']
            regra_nova = regra.Regra(campeonato=campeonato,vencedor=vencedor, golCasa=golCasa, golVisitante=golVisitante)
            regra_service.editar_regra(regra_antiga, regra_nova)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        regra = regra_service.listar_regra_id(id)
        regra_service.remover_regra(regra)
        return Response(status=status.HTTP_204_NO_CONTENT)


    def patch(self, request, id, format=None):
        regra = regra_service.listar_regra_id(id)
        serializer = regra_serializer.RegraSerializer(regra, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(force_update=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

