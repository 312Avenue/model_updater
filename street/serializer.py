from rest_framework import serializers
from .models import Street, Home


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = '__all__'

    def to_representation(self, instance):
        represent = super().to_representation(instance)
        return represent


class StreetSerializer(serializers.ModelSerializer):    
    homes = HomeSerializer(many=True, read_only=True)

    class Meta:
        model = Street
        fields = '__all__'
