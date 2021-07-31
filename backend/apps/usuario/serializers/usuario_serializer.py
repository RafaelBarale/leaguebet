# Utilizando o modo de autenticação padrão do django (auth)

from rest_framework import serializers
from django.contrib.auth.models import User


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        # Utilizando o modelo padrão do auth no django
        model = User
        # passando apenas os campos necessarios de edição
        fields = ('username', 'password')

    # Sobescrevendo o metodo padrão create
    def create(self, validated_data):
        # Retorno padrão
        # return super().create(validated_data)

        # validated_data = dados validos na requisição (fields da classe)
        user = super(UsuarioSerializer, self).create(validated_data)

        # criptografando o password antes de gravar
        user.set_password(validated_data['password'])

        # salvando o usuario criado no banco
        user.save()

        return user
