from django import forms
from . import models

class SensorForm(forms.ModelForm):
    class Meta:
        model = models.Sensor
        fields = (
            'equipmentID', 'value'
            )
    
    def clean(self):
        #cleaned_data = self.cleaned_data
        return super().clean()
    