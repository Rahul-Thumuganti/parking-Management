# Generated by Django 4.2.6 on 2023-10-18 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pkapk', '0061_remove_add_vehicle_vehicle_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_vehicle',
            name='vehicle_type',
            field=models.CharField(default=True, max_length=100),
        ),
    ]
