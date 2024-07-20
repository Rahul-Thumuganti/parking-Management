# Generated by Django 4.2.6 on 2023-10-18 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pkapk', '0046_remove_add_vehicle_parking_charge'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_vehicle',
            name='parking_charge',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='add_vehicle',
            name='parking_area_no',
            field=models.CharField(default=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='add_vehicle',
            name='vehicle_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pkapk.category'),
        ),
    ]
