# Arquivos serializer trabalha da mesma
# maneira que o forms, buscando o objeto e validando com o models
from rest_framework.reverse import reverse
from rest_framework import serializers
from ..models import Regra


class RegraSerializer(serializers.ModelSerializer):
    # links = serializers.SerializerMethodField()


    class Meta:
        model = Regra
        fields = ('id', 'campeonato', 'vencedor', 'golCasa', 'golVisitante', )
        # fields = ('id', 'usuario', 'campeonato', 'rodada', 'links', )
