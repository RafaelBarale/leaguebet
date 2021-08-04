from rest_framework.response import Response
from rest_framework.views import APIView
from ..services import apostajogo_service
from ..serializers import apostajogo_serializer
from rest_framework import status
from ..entidades import apostajogo

class ApostaJogoList(APIView):
    def get(self, request, format=None):
        aposta = apostajogo_service.listar_apostageral()
        serializer = apostajogo_serializer.ApostaJogoSerializer(aposta, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 

    def post(self, request, format=None):
        serializer = apostajogo_serializer.ApostaJogoSerializer(data=request.data)
        if serializer.is_valid():
            gol_casa = serializer.validated_data["gol_casa"]
            gol_visitante = serializer.validated_data['gol_visitante']
            usuario = serializer.validated_data["usuario"]
            jogo = serializer.validated_data['jogo']
            aposta_nova = apostajogo.ApostaJogo(gol_casa=gol_casa,gol_visitante=gol_visitante, usuario=usuario, jogo=jogo)
            apostajogo_service.cadastrar_apostajogo(aposta_nova)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ApostaJogoDetails(APIView):
    def get(self, request, id, format=None):
        aposta = apostajogo_service.listar_apostajogo_id(id)
        serializer = apostajogo_serializer.ApostaJogoSerializer(aposta)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id, format=None):
        aposta_antiga = apostajogo_service.listar_apostajogo_id(id)
        serializer = apostajogo_serializer.ApostaJogoSerializer(aposta_antiga, data=request.data)
        if serializer.is_valid():
            gol_casa = serializer.validated_data["gol_casa"]
            gol_visitante = serializer.validated_data['gol_visitante']
            aposta = serializer.validated_data["aposta"]
            jogo = serializer.validated_data['jogo']
            aposta_nova = apostajogo.Aposta(gol_casa=gol_casa,gol_visitante=gol_visitante, aposta=aposta, jogo=jogo)
            apostajogo_service.editar_aposta(aposta_antiga, aposta_nova)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        aposta = apostajogo_service.listar_apostajogo_id(id)
        apostajogo_service.remover_apostajogo(aposta)
        return Response(status=status.HTTP_204_NO_CONTENT)


    def patch(self, request, id, format=None):
        aposta = apostajogo_service.listar_apostajogo_id(id)
        serializer = apostajogo_serializer.ApostaJogoSerializer(aposta, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(force_update=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ApostaJogoCamp(APIView):
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
            lista_aposta = apostajogo_service.listar_apostajogo(jogo=jogo, usuario=usuario)
        elif rodada is not None:
            lista_aposta = apostajogo_service.listar_apostajogo_rodada(rodada=rodada, usuario=usuario)
        else:
            lista_aposta = apostajogo_service.listar_apostajogo_usuario(usuario=usuario)

        serializer = apostajogo_serializer.ApostaJogoSerializer(lista_aposta, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
