from rest_framework import serializers

from .models import Candidatos, Cidades, Estado, Urnas


class UrnaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Urnas
        exclude = ['candidato']


class CandidatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidatos
        fields = '__all__'


class CidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cidades
        exclude = ['urna', 'nome']


class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        exclude = ['cidade']
