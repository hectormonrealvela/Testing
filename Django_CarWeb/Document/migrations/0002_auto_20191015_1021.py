# Generated by Django 2.1.1 on 2019-10-15 10:21

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Document', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='gps_lat',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(decimal_places=3, max_digits=10), blank=True, null=True, size=3),
        ),
        migrations.AlterField(
            model_name='document',
            name='gps_long',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(decimal_places=3, max_digits=10), blank=True, null=True, size=3),
        ),
    ]
