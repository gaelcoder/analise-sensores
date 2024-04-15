from django.contrib import admin
from sensorizador import models

@admin.register(models.Sensor)

class SensorAdmin(admin.ModelAdmin):
    list_display = 'equipmentID', 'timestamp', 'value'
    ordering = '-timestamp',
    search_fields = 'equipmentID',
    list_per_page = 30
    list_max_show_all = 70
# Register your models here.
