from django.db import models

# Create your models here.
class Vehicle(models.Model):
    EURO_CATEGORY_CHOICES = [
        (1, "LOW"),
        (2, "SEMI-LOW"),
        (3, "MEDIUM"),
        (4, "SENIOR"),
        (5, "MODERATE"),
    ]

    vehicle_id = models.AutoField(primary_key=True, unique=True)
    brand = models.CharField("Brand", max_length=60)
    model = models.CharField("Model", max_length=60)
    horse_power = models.IntegerField("Horse Power", null=False, blank=False)
    build_year = models.DateField("Date", auto_now_add=True)
    euro_category = models.IntegerField(
        "Euro Category", choices=EURO_CATEGORY_CHOICES, default=1
    )
    price = models.IntegerField("Price", null=False, blank=False, default=0)

    def __str__(self):
        return f"{self.brand} {self.model} - {self.euro_category} - {self.build_year}"
