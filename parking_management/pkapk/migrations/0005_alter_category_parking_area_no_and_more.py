# Generated by Django 4.2.6 on 2023-10-13 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pkapk', '0004_remove_a_dmin_a_id_remove_add_vehicle_v_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='parking_area_no',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='category',
            name='parking_charge',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='category',
            name='vehicle_limit',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='category',
            name='vehicle_type',
            field=models.CharField(max_length=100),
        ),
    ]
