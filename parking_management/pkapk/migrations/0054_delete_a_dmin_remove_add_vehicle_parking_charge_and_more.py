# Generated by Django 4.2.6 on 2023-10-18 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pkapk', '0053_a_dmin_add_vehicle_parking_charge_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='a_dmin',
        ),
        migrations.RemoveField(
            model_name='add_vehicle',
            name='parking_charge',
        ),
        migrations.RemoveField(
            model_name='add_vehicle',
            name='vehicle_type',
        ),
    ]
