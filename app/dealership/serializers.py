from rest_framework import serializers

from .models import Cars, Trucks


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = [
            "brand",
            "model",
            "horse_power",
            "build_year",
            "euro_category",
            "vehicle_type",
            "price",
        ]


class TruckSerializer(serializers.ModelSerializer):
    created_time = serializers.CharField(source="get_created_time", required=False)

    class Meta:
        model = Trucks
        fields = [
            "brand",
            "model",
            "horse_power",
            "build_year",
            "max_load",
            "vehicle_type",
            "price",
            "created_time",
        ]
