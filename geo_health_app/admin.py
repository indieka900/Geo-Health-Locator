from django.contrib import admin

from django.contrib.auth.models import Group
from geo_health_app.models import (Disease, Patient, TreatPatient)


@admin.register(Disease)
class DiseaseAdmin(admin.ModelAdmin):
    search_fields = ["reporter",]
    list_display = ("id","symptoms", "reported_to", 
                    "latitude", "longitude",
                    "reported_at")
    
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    search_fields = ["full_name",]
    list_display = ("full_name", "age", "health_situation")

@admin.register(TreatPatient)
class TreatPatientAdmin(admin.ModelAdmin):
    search_fields = ["full_name",]
    list_display = ("full_name", "op_number", "age", "height",
                    "bp_reading", "glucose_level", "weight_reading",
                    "temperature_reading", "symptoms", "prescribe_lab_test", 
                    "lab_test_results", "drug_prescription", "treatment_status")