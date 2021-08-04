# Arquivos serializer trabalha da mesma
# maneira que o forms, buscando o objeto e validando com o models
from rest_framework.reverse import reverse
from rest_framework import serializers
from ..models import ApostaJogo


class ApostaJogoSerializer(serializers.ModelSerializer):
    # links = serializers.SerializerMethodField()

    class Meta:
        model = ApostaJogo
        fields = ('id', 'gol_casa', 'gol_visitante', 'aposta', 'jogo', )
        # fields = ('id', 'usuario', 'campeonato', 'rodada', 'links', )
