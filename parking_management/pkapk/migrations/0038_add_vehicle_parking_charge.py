# Generated by Django 4.2.6 on 2023-10-18 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pkapk', '0037_add_vehicle_vehicle_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_vehicle',
            name='parking_charge',
            field=models.CharField(default='Default Parking Charge', max_length=200),
        ),
    ]
