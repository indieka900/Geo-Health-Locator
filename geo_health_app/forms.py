from geo_health_app.models import Disease, Patient
from django import forms

class ReportDiseaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['latitude'].widget.attrs.update({'id': 'latitude'})
        self.fields['longitude'].widget.attrs.update({'id': 'longitude'})
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
    class Meta:
        model = Disease
        fields = ("symptoms", "latitude", "longitude",)
        
class OrderAmbulanceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control pl-5'})
    class Meta:
        model = Patient
        exclude = ["reporter"]