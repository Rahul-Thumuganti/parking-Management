# Generated by Django 4.2.6 on 2023-10-18 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pkapk', '0058_alter_add_vehicle_parking_charge_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_vehicle',
            name='parking_charge',
        ),
        migrations.RemoveField(
            model_name='add_vehicle',
            name='vehicle_type',
        ),
        migrations.AlterField(
            model_name='add_vehicle',
            name='parking_area_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pkapk.category'),
        ),
    ]
