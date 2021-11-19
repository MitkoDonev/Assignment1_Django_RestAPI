import json
from django.shortcuts import render
from django.http import JsonResponse

from .models import Dealership
from vehicle.models import Vehicle


def convert_as_dict(list_entry):
    return [
        {
            "brand": entry.vehicle.brand,
            "model": entry.vehicle.model,
            "year": entry.vehicle.build_year,
            "category": entry.vehicle.euro_category,
            "price": entry.vehicle.price,
            "type": entry.vehicle_type,
            "location": entry.location,
        }
        for entry in list_entry
    ]


# Create your views here.
def get_entries(request):
    entries = Dealership.objects.all()
    entries_dict = convert_as_dict(entries)

    return JsonResponse(entries_dict, safe=False)


def create_entry(request):
    body_unicode = request.body.decode("utf-8")
    body = json.loads(body_unicode)

    new_vehicle = Vehicle(
        brand=body["vehicle"]["brand"],
        model=body["vehicle"]["model"],
        horse_power=body["vehicle"]["horse_power"],
        build_year=body["vehicle"]["build_year"],
        euro_category=body["vehicle"]["euro_category"],
        price=body["vehicle"]["price"],
    )
    new_vehicle.save()

    description = body["description"]
    vehicle_type = body["vehicle_type"]
    location = body["location"]

    new_entry = Dealership(
        vehicle=new_vehicle,
        description=description,
        vehicle_type=vehicle_type,
        location=location,
    )
    new_entry.save()

    entries = Dealership.objects.all()
    entries_dict = convert_as_dict(entries)

    return JsonResponse(entries_dict, safe=False)
