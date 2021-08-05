# Arquivos serializer trabalha da mesma
# maneira que o forms, buscando o objeto e validando com o models
from rest_framework.reverse import reverse
from rest_framework import serializers
from ..models import Rodada


class RodadaSerializer(serializers.ModelSerializer):
    # links = serializers.SerializerMethodField()

    class Meta:
        model = Rodada
        fields = ('id', 'numero', 'campeonato', 'fechada' )
        # fields = ('id', 'numero', 'campeonato', 'links', )
