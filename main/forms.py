from django import forms

class TemperatureForm(forms.Form):

    sensor = forms.CharField(required=True)
    value = forms.IntegerField(required=True)