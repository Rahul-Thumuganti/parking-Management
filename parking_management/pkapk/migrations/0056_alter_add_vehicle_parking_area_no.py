# Generated by Django 4.2.6 on 2023-10-18 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pkapk', '0055_add_vehicle_vehicle_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_vehicle',
            name='parking_area_no',
            field=models.CharField(max_length=200),
        ),
    ]
