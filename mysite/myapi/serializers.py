from rest_framework import serializers
from .models import Juego
from .models import Party
from .models import PartyPlayers
from .models import PartyChat


class JuegoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Juego
        fields = '__all__'


class PartySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Party
        fields = ('nombre', 'descripcion')


class PartyPlayersSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartyPlayers
        fields = ('party', 'jugador')


class PartyChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartyChat
        fields = ('sala', 'jugador', 'comentario')
