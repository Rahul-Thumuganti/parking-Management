# Generated by Django 4.2.6 on 2023-10-16 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pkapk', '0013_alter_add_vehicle_vehicle_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_vehicle',
            name='parking_charge',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehicles_with_charge', to='pkapk.category'),
        ),
    ]
