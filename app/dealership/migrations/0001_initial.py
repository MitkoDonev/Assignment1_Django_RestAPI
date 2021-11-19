# Generated by Django 3.2.7 on 2021-11-19 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("vehicle", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Dealership",
            fields=[
                (
                    "entry_id",
                    models.AutoField(
                        editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, max_length=200, verbose_name="Description"
                    ),
                ),
                (
                    "vehicle_type",
                    models.CharField(
                        choices=[(1, "NEW"), (2, "USED"), (3, "SCRAP")],
                        default=2,
                        max_length=10,
                        verbose_name="Vehicle Type",
                    ),
                ),
                (
                    "vehicle",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="vehicle.vehicle",
                    ),
                ),
            ],
        ),
    ]
