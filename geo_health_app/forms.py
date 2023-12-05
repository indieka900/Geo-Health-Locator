from geo_health_app.models import Disease, Patient, TreatPatient
from django import forms

class ReportDiseaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['latitude'].widget.attrs['readonly'] = True
        self.fields['longitude'].widget.attrs['readonly'] = True
        self.fields['latitude'].widget.attrs['id'] = 'latitude'
        self.fields['longitude'].widget.attrs['id'] = 'longitude'

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
    class Meta:
        model = Disease
        fields = ("symptoms", "latitude", "longitude",)
        
        
class OrderAmbulanceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['latitude'].widget.attrs['readonly'] = True
        self.fields['longitude'].widget.attrs['readonly'] = True
        self.fields['type_l'].widget = forms.HiddenInput()
        self.fields['latitude'].widget.attrs['id'] = 'latitude'
        self.fields['longitude'].widget.attrs['id'] = 'longitude'
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control pl-2'})
    class Meta:
        model = Patient
        exclude = ["reporter","reported_to"]

class TreatPatientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": 'form-control'})

    class Meta:
        model = TreatPatient
        fields = ("full_name", "ip_op_number", "age", "height",
                    "bp_reading", "glucose_level", "weight_reading",
                    "temperature_reading", "symptoms", "prescribe_lab_test" 
                    # "lab_test_results", "drug_prescription", "treatment_status"
                    )