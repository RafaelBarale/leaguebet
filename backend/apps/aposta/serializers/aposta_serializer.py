# Arquivos serializer trabalha da mesma
# maneira que o forms, buscando o objeto e validando com o models
from rest_framework.reverse import reverse
from rest_framework import serializers
from apps.campeonato.services import jogo_service, rodada_service
from ..models import Aposta


class ApostaSerializer(serializers.ModelSerializer):
    # links = serializers.SerializerMethodField()


    class Meta:
        model = Aposta
        fields = ('id', 'gol_casa', 'gol_visitante', 'usuario', 'jogo', )
        # fields = ('id', 'usuario', 'campeonato', 'rodada', 'links', )

        """
        Utilizado para criar validação com mais de um campo.
        def validate(self, data):

            if data['start'] > data['finish']:
                raise serializers.ValidationError("finish must occur after start")
        """

    def validate_jogo(self, value):
        # validação de rodada fechada ou não
        if value.rodada.fechada:
            raise serializers.ValidationError("Rodada fechada, não pode mais apostar")

        return value