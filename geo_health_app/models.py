from django.db import models
from accounts.models import User, Hospital
from django.utils.translation import gettext as _

class Disease(models.Model):
    reported_to = models.CharField(_("Reported to"), max_length=50, default='Mwatate Sub-County Hospital')
    reporter = models.ManyToManyField(User)
    symptoms = models.TextField( _("Symptoms"), blank=True, null=True)
    latitude = models.FloatField(_("latitude"),
                                 blank=True, null=True)
    longitude = models.FloatField(_("longitude"),
                                  blank=True, null=True)
    reported_at = models.DateTimeField(auto_now_add=True)


class Patient(Disease):
    full_name = models.CharField(_("full name"), max_length=100,
                                 blank=False, null=False)
    age = models.IntegerField(_("age"), blank=True, null=True)
    health_situation = models.TextField(_("health situation"), max_length=1000,
                                        blank=True, null=True)

class TreatPatient(Patient):
    treament_status_choices = (("Not Treated", "Not Treated"),
                                ("Treated", "Treated"),
                                ("In Progress", "In Progress"))
    op_number = models.IntegerField(_("OP Number"), max_length=100, blank=False, null=False)
    height = models.FloatField(_("height"), max_length=500, blank=False, null=False)
    bp_reading = models.FloatField(_("BP Reading"), max_length=1000, blank=False, null=False)
    glucose_level = models.FloatField(_("glucose level"), max_length=1000, blank=False, null=False)
    weight_reading = models.FloatField(_("weight reading (kg)"), max_length=1000, blank=False, null=False)
    temperature_reading = models.FloatField(_("temperature reading (degree celcius)"), max_length=1000, blank=False, null=False)
    prescribe_lab_test = models.TextField(_("prescribe lab test"), blank=True, null=True)
    lab_test_results = models.TextField(_("lab test results"), blank=True, null=True)
    drug_prescription = models.TextField(_("drug prescription"), blank=True, null=True)
    treatment_status = models.CharField(_("treatment status"), max_length=50, choices=treament_status_choices, default="Not Treated")
