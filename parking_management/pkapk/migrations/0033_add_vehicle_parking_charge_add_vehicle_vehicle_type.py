# Generated by Django 4.2.6 on 2023-10-18 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pkapk', '0032_remove_add_vehicle_parking_charge_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_vehicle',
            name='parking_charge',
            field=models.CharField(default=True, max_length=200),
        ),
        migrations.AddField(
            model_name='add_vehicle',
            name='vehicle_type',
            field=models.CharField(default=True, max_length=200),
        ),
    ]
