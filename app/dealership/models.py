from django.db import models

from datetime import datetime

# Create your models here.
class Vehicles(models.Model):
    VEHICLE_TYPES = [(1, "NEW"), (2, "USED"), (3, "SCRAP")]

    brand = models.CharField("Brand", max_length=60)
    model = models.CharField("Model", max_length=60)
    horse_power = models.IntegerField("Horse Power", null=False, blank=False)
    build_year = models.DateField("Date")
    vehicle_type = models.CharField(
        "Vehicle Type", choices=VEHICLE_TYPES, default=2, max_length=10
    )
    location = models.CharField("Location", max_length=60, null=True, blank=True)
    price = models.IntegerField("Price", null=False, blank=False, default=0)

    class Meta:
        abstract = True
        ordering = ['price']

    @property
    def get_created_time(self):
        now = datetime.now()
        current = now.strftime("%H:%M:%S")
        return current

    def __str__(self):
        return f"{self.brand} {self.model} : {self.price}"

class Cars(Vehicles):
    EURO_CATEGORY_CHOICES = [
        (1, "LOW"),
        (2, "SEMI-LOW"),
        (3, "MEDIUM"),
        (4, "SENIOR"),
        (5, "MODERATE"),
    ]

    euro_category = models.CharField(
        "Euro Category", choices=EURO_CATEGORY_CHOICES, default=1, max_length=10
    )

class Trucks(Vehicles):
    MAX_LOAD = [
        (1, 1000),
        (2, 2000),
        (3, 3000),
        (4, 4000),
        (5, 5000),
        (5, 6000),
    ]

    max_load = models.IntegerField("Euro Category", choices=MAX_LOAD, default=1)