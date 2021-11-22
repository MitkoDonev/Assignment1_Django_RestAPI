from django.db import models

# Create your models here.
class Trucks(models.Model):
    MAX_LOAD = [
        (1, 1000),
        (2, 2000),
        (3, 3000),
        (4, 4000),
        (5, 5000),
        (5, 6000),
    ]

    brand = models.CharField("Brand", max_length=60)
    model = models.CharField("Model", max_length=60)
    horse_power = models.IntegerField("Horse Power", null=False, blank=False)
    build_year = models.DateField("Date")
    max_load = models.IntegerField("Euro Category", choices=MAX_LOAD, default=1)
    price = models.IntegerField("Price", null=False, blank=False, default=0)

    def __str__(self):
        return f"{self.brand} {self.model} - {self.euro_category} - {self.build_year}"
