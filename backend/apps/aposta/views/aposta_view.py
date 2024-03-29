from rest_framework.response import Response
from rest_framework.views import APIView
from ..services import aposta_service
from ..serializers import aposta_serializer
from rest_framework import status
from ..entidades import aposta


class ApostaList(APIView):
    def get(self, request, format=None):
        aposta = aposta_service.listar_apostageral()
        serializer = aposta_serializer.ApostaSerializer(aposta, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 

    def post(self, request, format=None):
        serializer = aposta_serializer.ApostaSerializer(data=request.data)
        if serializer.is_valid():
            gol_casa = serializer.validated_data["gol_casa"]
            gol_visitante = serializer.validated_data['gol_visitante']
            usuario = serializer.validated_data["usuario"]
            jogo = serializer.validated_data['jogo']
            aposta_nova = aposta.Aposta(gol_casa=gol_casa,gol_visitante=gol_visitante, usuario=usuario, jogo=jogo)
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
            gol_casa = serializer.validated_data["gol_casa"]
            gol_visitante = serializer.validated_data['gol_visitante']
            usuario = serializer.validated_data["usuario"]
            jogo = serializer.validated_data['jogo']
            aposta_nova = aposta.Aposta(gol_casa=gol_casa,gol_visitante=gol_visitante, usuario=usuario, jogo=jogo)
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
        jogo = query_params.get('jogo', None)
        usuario = query_params.get('usuario', None)
        rodada = query_params.get('rodada', None)
        if jogo is None and usuario is None and rodada is None:
            errors = {
                'ERROR': "Pelo menos um dos campos e obrigatorio 'jogo', 'usuario', 'rodada' "
            }
            return Response(errors,status=status.HTTP_400_BAD_REQUEST)

        if jogo is not None:
            lista_aposta = aposta_service.listar_aposta(jogo=jogo, usuario=usuario)
        elif rodada is not None:
            lista_aposta = aposta_service.listar_aposta_rodada(rodada=rodada, usuario=usuario)
        else:
            lista_aposta = aposta_service.listar_aposta_usuario(usuario=usuario)

        serializer = aposta_serializer.ApostaSerializer(lista_aposta, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
