# Generated by Django 4.2.6 on 2023-10-17 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pkapk', '0025_alter_add_vehicle_parking_charge_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_vehicle',
            name='parking_charge',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='add_vehicle',
            name='vehicle_type',
            field=models.CharField(max_length=200),
        ),
    ]
