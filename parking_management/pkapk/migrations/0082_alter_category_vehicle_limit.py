# Generated by Django 4.2.6 on 2023-10-19 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pkapk', '0081_alter_category_vehicle_limit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='vehicle_limit',
            field=models.CharField(max_length=200),
        ),
    ]
