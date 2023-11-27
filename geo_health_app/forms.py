from geo_health_app.models import Disease, Patient, TreatPatient
from django import forms

class ReportDiseaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['latitude'].widget.attrs.update({'id': 'latitude'})
        # self.fields['longitude'].widget.attrs.update({'id': 'longitude'})
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
    class Meta:
        model = Disease
        fields = ("symptoms", "latitude", "longitude",)
        
        
class OrderAmbulanceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control pl-2'})
    class Meta:
        model = Patient
        exclude = ["reporter"]

class TreatPatientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": 'form-control'})

    class Meta:
        model = TreatPatient
        fields = ("full_name", "op_number", "age", "height",
                    "bp_reading", "glucose_level", "weight_reading",
                    "temperature_reading", "symptoms", "prescribe_lab_test" 
                    # "lab_test_results", "drug_prescription", "treatment_status"
                    )