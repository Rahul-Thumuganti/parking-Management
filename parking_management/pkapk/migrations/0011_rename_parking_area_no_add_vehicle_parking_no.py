# Generated by Django 4.2.6 on 2023-10-16 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pkapk', '0010_alter_add_vehicle_parking_area_no'),
    ]

    operations = [
        migrations.RenameField(
            model_name='add_vehicle',
            old_name='parking_area_no',
            new_name='parking_no',
        ),
    ]
