# Arquivos serializer trabalha da mesma
# maneira que o forms, buscando o objeto e validando com o models
from rest_framework.reverse import reverse
from rest_framework import serializers
from ..models import Jogo


class JogoSerializer(serializers.ModelSerializer):
    # links = serializers.SerializerMethodField()

    def validate(self, attrs):
        instance = Jogo(**attrs)
        instance.clean()
        return attrs

    class Meta:
        model = Jogo
        fields = ('id', 'gols_casa', 'gols_visitante', 'clube_casa', 'clube_visitante', 'rodada', 'campeonato', )
        # fields = ('id', 'gols_casa', 'gols_visitante', 'clube_casa', 'clube_visitante', 'rodada', 'campeonato', 'links', )
