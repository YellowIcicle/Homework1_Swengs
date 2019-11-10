from rest_framework import serializers
from HW1.HW1.models import Country, Producer, Smartphone


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name']


class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = ['id', 'name', 'founded', 'headquaters', 'founder']


class SmartphoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Smartphone
        fields = ['id', 'name', 'OS', 'release_date', 'description', 'price', 'producer']