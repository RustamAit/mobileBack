from rest_framework import serializers

from api.models import *


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"


class GameDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameData
        fields = "__all__"


class GameSessionSerializer(serializers.ModelSerializer):
    players = PersonSerializer(many=True)
    class Meta:
        model = GameSession
        fields = "__all__"

