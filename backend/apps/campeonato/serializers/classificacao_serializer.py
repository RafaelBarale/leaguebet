# Arquivos serializer trabalha da mesma
# maneira que o forms, buscando o objeto e validando com o models
from rest_framework.reverse import reverse
from rest_framework import serializers
from ..models import Classificacao


class ClassificacaoSerializer(serializers.ModelSerializer):
    # links = serializers.SerializerMethodField()

    class Meta:
        model = Classificacao
        fields = ('id', 'pontos', 'jogos', 'vitorias', 'derrotas', 'empates', 'gols_pro', 'gols_contra', 'campeonato','clube' )
        # fields = ('id', 'pontos', 'jogos', 'vitorias', 'derrotas', 'empates', 'gols_pro', 'gols_contra', 'campeonato', 'links', )
