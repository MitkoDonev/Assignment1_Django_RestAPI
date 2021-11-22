from django.db import models

from cars.models import Cars
from trucks.models import Trucks

# Create your models here.
class Dealership(models.Model):
    VEHICLE_TYPE = [(1, "NEW"), (2, "USED"), (3, "SCRAP")]
    VEHICLE_CATEGORY = [(1, "CAR"), (2, "TRUCK")]

    description = models.TextField("Description", max_length=200, blank=True)
    vehicle_category = models.CharField(
        "Vehicle Category", choices=VEHICLE_CATEGORY, default=1, max_length=10
    )

    car = models.ForeignKey(
        Cars, related_name="cars", on_delete=models.CASCADE, null=True, blank=True
    )
    truck = models.ForeignKey(
        Trucks, related_name="trucks", on_delete=models.CASCADE, null=True, blank=True
    )

    vehicle_type = models.CharField(
        "Vehicle Type", choices=VEHICLE_TYPE, default=2, max_length=10
    )
    location = models.CharField("Location", max_length=60, null=True, blank=True)

    def __str__(self):
        return f"{self.vehicle_category}"
