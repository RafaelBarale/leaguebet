from rest_framework.response import Response
from rest_framework.views import APIView
from ..services import apostajogo_service
from ..serializers import apostajogo_serializer
from rest_framework import status
from ..entidades import apostajogo

class ApostaList(APIView):
    def get(self, request, format=None):
        aposta = aposta_service.listar_apostas()
        serializer = aposta_serializer.ApostaSerializer(aposta, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 

    def post(self, request, format=None):
        serializer = aposta_serializer.ApostaSerializer(data=request.data)
        if serializer.is_valid():
            
            usuario = serializer.validated_data["usuario"]
            rodada = serializer.validated_data['rodada']
            aposta_nova = aposta.Aposta(usuario=usuario, rodada=rodada)
            aposta_service.cadastrar_aposta(aposta_nova)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ApostaDetails(APIView):
    def get(self, request, id, format=None):
        aposta = aposta_service.listar_aposta_id(id)
        serializer = aposta_serializer.ApostaSerializer(aposta)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id, format=None):
        aposta_antiga = aposta_service.listar_aposta_id(id)
        serializer = aposta_serializer.ApostaSerializer(aposta_antiga, data=request.data)
        if serializer.is_valid():
            
            usuario = serializer.validated_data["usuario"]
            rodada = serializer.validated_data['rodada']
            aposta_nova = aposta.Aposta(usuario=usuario, rodada=rodada)
            aposta_service.editar_aposta(aposta_antiga, aposta_nova)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        aposta = aposta_service.listar_aposta_id(id)
        aposta_service.remover_aposta(aposta)
        return Response(status=status.HTTP_204_NO_CONTENT)


    def patch(self, request, id, format=None):
        aposta = aposta_service.listar_aposta_id(id)
        serializer = aposta_serializer.ApostaSerializer(aposta, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(force_update=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ApostaCamp(APIView):
    def get(self, request, format=None):
        query_params = request.query_params
        campeonato = query_params.get('campeonato', None)
        usuario = query_params.get('usuario', None)
        rodada = query_params.get('rodada', None)
        if campeonato is None and usuario is None and rodada is None:
            errors = {
                'campeonato': "Campo Obrigatorio",
                'usuario': "Campo obrigatorio",
                'rodada': 'Campo Obrigatorio'
            }
            return Response(errors,status=status.HTTP_400_BAD_REQUEST)

        lista_aposta = aposta_service.listar_aposta_campeonato_rodada(usuario=usuario, campeonato=campeonato, rodada=rodada)
        serializer = aposta_serializer.ApostaSerializer(lista_aposta, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
