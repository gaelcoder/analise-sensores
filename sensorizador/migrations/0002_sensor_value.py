# Generated by Django 5.0.4 on 2024-04-14 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensorizador', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='value',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
