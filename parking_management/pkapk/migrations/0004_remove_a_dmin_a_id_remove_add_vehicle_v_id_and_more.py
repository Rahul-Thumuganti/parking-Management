# Generated by Django 4.2.6 on 2023-10-12 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pkapk', '0003_add_vehicle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='a_dmin',
            name='a_id',
        ),
        migrations.RemoveField(
            model_name='add_vehicle',
            name='v_id',
        ),
        migrations.RemoveField(
            model_name='category',
            name='cat_id',
        ),
    ]
