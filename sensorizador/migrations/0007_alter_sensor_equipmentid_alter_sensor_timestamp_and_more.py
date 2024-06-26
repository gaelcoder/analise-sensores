# Generated by Django 5.0.4 on 2024-04-15 06:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensorizador', '0006_alter_sensor_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='equipmentID',
            field=models.CharField(max_length=50, verbose_name='ID do Equipamento'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 15, 6, 16, 39, 987101, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='value',
            field=models.FloatField(verbose_name='Valor'),
        ),
    ]
