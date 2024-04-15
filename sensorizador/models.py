from django.db import models
from django.utils import timezone
from datetime import datetime

class Sensor(models.Model):
    equipmentID = models.CharField(max_length=50, verbose_name='ID do Equipamento')
    timestamp = models.DateTimeField(default=timezone.now())
    value = models.FloatField(verbose_name='Valor')

    def __str__(self) -> str:
        return f'{self.equipmentID}'