# Generated by Django 4.2.6 on 2023-10-18 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pkapk', '0071_add_vehicle_vehicle_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_vehicle',
            name='vehicle_type',
            field=models.CharField(max_length=100),
        ),
    ]
