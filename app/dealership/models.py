from django.db import models
from vehicle.models import Vehicle

# Create your models here.
class Dealership(models.Model):
    VEHICLE_TYPE = [(1, "NEW"), (2, "USED"), (3, "SCRAP")]

    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    description = models.TextField("Description", max_length=200, blank=True)
    vehicle_type = models.CharField(
        "Vehicle Type", choices=VEHICLE_TYPE, default=2, max_length=10
    )
    location = models.CharField("Location", max_length=60, null=True, blank=True)

    def __str__(self):
        return f"{self.vehicle} - {self.vehicle_type}"
