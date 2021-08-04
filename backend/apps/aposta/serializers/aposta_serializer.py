# Arquivos serializer trabalha da mesma
# maneira que o forms, buscando o objeto e validando com o models
from rest_framework.reverse import reverse
from rest_framework import serializers
from ..models import Aposta


class ApostaSerializer(serializers.ModelSerializer):
    # links = serializers.SerializerMethodField()

    class Meta:
        model = Aposta
        fields = ('id', 'gol_casa', 'gol_visitante', 'usuario', 'jogo', )
        # fields = ('id', 'usuario', 'campeonato', 'rodada', 'links', )
