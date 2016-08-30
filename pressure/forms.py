from django import forms
from pressure.models import Measurment


class MeasurmentForm(forms.ModelForm):
    # systolic = forms.FloatField(help_text='Enter systolic measurment')
    # diastolic = forms.FloatField(help_text='Enter diastolic measurment')
    # date = forms.DateField(widget=forms.HiddenInput())

    class Meta:
        model = Measurment
        fields = ('systolic', 'diastolic', )
