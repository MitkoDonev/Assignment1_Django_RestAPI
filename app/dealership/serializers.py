from django.db.models import fields
from rest_framework import serializers

from .models import Cars, Trucks

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = "__all__"

class TruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trucks
        fields = "__all__"