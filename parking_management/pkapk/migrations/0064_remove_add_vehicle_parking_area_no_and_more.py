# Generated by Django 4.2.6 on 2023-10-18 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pkapk', '0063_alter_add_vehicle_vehicle_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_vehicle',
            name='parking_area_no',
        ),
        migrations.AlterField(
            model_name='add_vehicle',
            name='vehicle_type',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pkapk.category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='vehicle_type',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
