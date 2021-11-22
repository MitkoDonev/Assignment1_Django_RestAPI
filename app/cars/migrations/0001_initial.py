# Generated by Django 3.2.7 on 2021-11-22 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=60, verbose_name='Brand')),
                ('model', models.CharField(max_length=60, verbose_name='Model')),
                ('horse_power', models.IntegerField(verbose_name='Horse Power')),
                ('build_year', models.DateField(verbose_name='Date')),
                ('euro_category', models.CharField(choices=[(1, 'LOW'), (2, 'SEMI-LOW'), (3, 'MEDIUM'), (4, 'SENIOR'), (5, 'MODERATE')], default=1, max_length=10, verbose_name='Euro Category')),
                ('price', models.IntegerField(default=0, verbose_name='Price')),
            ],
        ),
    ]
