# Generated by Django 4.2.6 on 2023-10-18 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pkapk', '0056_alter_add_vehicle_parking_area_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_vehicle',
            name='parking_charge',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='add_vehicle',
            name='vehicle_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pkapk.category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='parking_area_no',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='category',
            name='vehicle_type',
            field=models.CharField(max_length=200),
        ),
    ]
