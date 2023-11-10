from django.db import models
from accounts.models import User, Hospital
from django.utils.translation import gettext as _

class Disease(models.Model):
    reporter = models.OneToOneField(User, 
                                    on_delete=models.CASCADE)
    symptoms = models.JSONField(default=list, blank=True, null=True)
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
