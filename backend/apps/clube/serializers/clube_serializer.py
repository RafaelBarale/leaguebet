# Arquivos serializer trabalha da mesma
# maneira que o forms, buscando o objeto e validando com o models
from rest_framework.reverse import reverse
from rest_framework import serializers
from ..models import Clube


class ClubeSerializer(serializers.ModelSerializer):
    #links = serializers.SerializerMethodField()

    class Meta:
        model = Clube
        fields = ('id', 'nome', 'nome_abreviado', 'estado', 'escudo', )
        # fields = ('id', 'nome', 'nome_abreviado', 'estado', 'escudo', 'links', )
