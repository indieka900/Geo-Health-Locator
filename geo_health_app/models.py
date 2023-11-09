# from django.db import models
# from accounts.models import User
# from django.utils.translation import gettext as _

# class Disease(models.Model):
#     reporter = models.OneToOneField(User, 
#                                     on_delete=models.CASCADE, unique=True)
#     symptoms = models.JSONField(default=list)
#     latitude = models.FloatField(_("latitude"),
#                                  blank=True, null=True)
#     longitude = models.FloatField(_("longitude"),
#                                   blank=True, null=True)
#     reported_at = models.DateTimeField(auto_now_add=True)


