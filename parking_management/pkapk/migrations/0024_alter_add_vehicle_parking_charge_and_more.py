# Generated by Django 4.2.6 on 2023-10-16 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pkapk', '0023_alter_add_vehicle_parking_charge_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_vehicle',
            name='parking_charge',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='vehicles_with_charge', to='pkapk.category'),
        ),
        migrations.AlterField(
            model_name='add_vehicle',
            name='vehicle_type',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='vehicle_type_vehicles', to='pkapk.category'),
        ),
    ]
