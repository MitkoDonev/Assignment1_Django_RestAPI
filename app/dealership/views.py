import json
from django.shortcuts import render
from django.http import JsonResponse

from .models import Dealership
from cars.models import Cars
from trucks.models import Trucks

# Create your views here.
def get_entries(request):
    if request.method != "GET":
        return JsonResponse({"message": "Wrong HTTP"}, safe=False, status=405)

    entries = Dealership.objects.all().values()
    result = [entries_values for entries_values in entries]

    return JsonResponse(result, safe=False, status=200)


def create_entry(request):

    if request.method != "POST":
        return JsonResponse({"message": "Wrong HTTP"}, safe=False, status=405)

    body_unicode = request.body.decode("utf-8")
    body = json.loads(body_unicode)

    new_entry = None

    if body["vehicle_category"].lower() == "car":
        car = Cars(
            brand=body["vehicle"]["brand"],
            model=body["vehicle"]["model"],
            horse_power=body["vehicle"]["horse_power"],
            build_year=body["vehicle"]["build_year"],
            euro_category=body["vehicle"]["euro_category"],
            price=body["vehicle"]["price"],
        )
        car.save()

        description = body["description"]
        vehicle_type = body["vehicle_type"]
        location = body["location"]

        new_entry = Dealership(
            car_id=car.id,
            vehicle_category=body["vehicle_category"],
            description=description,
            vehicle_type=vehicle_type,
            location=location,
        )
        new_entry.save()

    else:
        truck = Trucks(
            brand=body["vehicle"]["brand"],
            model=body["vehicle"]["model"],
            horse_power=body["vehicle"]["horse_power"],
            build_year=body["vehicle"]["build_year"],
            max_load=body["vehicle"]["max_load"],
            price=body["vehicle"]["price"],
        )

        truck.save()

        description = body["description"]
        vehicle_type = body["vehicle_type"]
        location = body["location"]

        new_entry = Dealership(
            truck_id=truck.id,
            vehicle_category=body["vehicle_category"],
            description=description,
            vehicle_type=vehicle_type,
            location=location,
        )
        new_entry.save()

    entry = Dealership.objects.filter(id=new_entry.id).values()

    result = [dealership_values for dealership_values in entry]

    return JsonResponse(result[0], safe=False, status=200)


def delete_entry(request, vehicle_type, vehicle_id):

    if request.method != "DELETE":
        return JsonResponse({"message": "Wrong HTTP"}, safe=False, status=405)

    message = f"Successfully deleted entry: {vehicle_type} - {vehicle_id}"
    status = 200

    if vehicle_type == "car":
        if Cars.objects.filter(id=vehicle_id).exists():
            entry = Cars.objects.get(id=vehicle_id)
            entry.delete()
        else:
            message = "ID does not exist"
            status = 404
    elif vehicle_type == "truck":
        if Trucks.objects.filter(id=vehicle_id).exists():
            entry = Trucks.objects.get(id=vehicle_id)
            entry.delete()
        else:
            message = "ID does not exist"
            status = 404
    else:
        message = "Vehicle Type does not exist"
        status = 404

    return JsonResponse({"message": message}, safe=False, status=status)


def edit_entry(request, vehicle_type, vehicle_id):
    if request.method != "PUT" and request.method != "PATCH":
        return JsonResponse({"message": "Wrong HTTP"}, safe=False, status=405)

    body_unicode = request.body.decode("utf-8")
    body = json.loads(body_unicode)

    message = f"Successfully edited entry: {vehicle_type} - {vehicle_id}"
    status = 200

    result = None

    if vehicle_type == "car":
        if Cars.objects.filter(id=vehicle_id).exists():
            Cars.objects.filter(id=vehicle_id).update(**body["vehicle"])
            entry = Cars.objects.filter(id=vehicle_id).values()
            result = [entry_values for entry_values in entry]
        else:
            message = "ID does not exist"
            status = 404
    elif vehicle_type == "truck":
        if Trucks.objects.filter(id=vehicle_id).exists():
            Trucks.objects.filter(id=vehicle_id).update(**body["vehicle"])
            entry = Trucks.objects.filter(id=vehicle_id).values()
            result = [entry_values for entry_values in entry]
        else:
            message = "ID does not exist"
            status = 200
    else:
        message = "Vehicle Type does not exist"
        status = 404

    return JsonResponse(
        {"message": message, "vehicle": result[0]}, safe=False, status=status
    )
