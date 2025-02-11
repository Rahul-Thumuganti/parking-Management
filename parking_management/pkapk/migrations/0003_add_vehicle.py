# Generated by Django 4.2.5 on 2023-10-11 07:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pkapk', '0002_a_dmin'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('v_id', models.TextField()),
                ('vehicle_no', models.TextField(max_length=200)),
                ('parking_area_no', models.TextField(max_length=200)),
                ('vehicle_type', models.TextField(max_length=200)),
                ('parking_charge', models.TextField(max_length=200)),
                ('status', models.TextField(max_length=200)),
                ('arrival_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
