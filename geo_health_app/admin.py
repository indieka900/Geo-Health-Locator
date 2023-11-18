from django.contrib import admin

from django.contrib.auth.models import Group
from geo_health_app.models import (Disease, Patient)


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