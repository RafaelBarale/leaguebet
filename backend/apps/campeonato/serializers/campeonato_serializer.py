# Arquivos serializer trabalha da mesma
# maneira que o forms, buscando o objeto e validando com o models
from rest_framework.reverse import reverse
from rest_framework import serializers
from ..models import Campeonato


class CampeonatoSerializer(serializers.ModelSerializer):
    # links = serializers.SerializerMethodField()

    class Meta:
        model = Campeonato
        fields = ('id', 'nome', 'temporada',)
        # fields = ('id', 'nome', 'temporada', 'links', )
