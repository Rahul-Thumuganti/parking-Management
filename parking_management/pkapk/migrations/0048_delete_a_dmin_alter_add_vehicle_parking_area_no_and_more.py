# Generated by Django 4.2.6 on 2023-10-18 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pkapk', '0047_add_vehicle_parking_charge_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='a_dmin',
        ),
        migrations.AlterField(
            model_name='add_vehicle',
            name='parking_area_no',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='add_vehicle',
            name='parking_charge',
            field=models.CharField(max_length=200),
        ),
    ]
