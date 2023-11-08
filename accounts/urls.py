from django.urls import path
from accounts.views import MedicalPersonellSignupView, CommunityMemberSignupView,VerifyEmail

app_name = 'accounts'

urlpatterns = [
    path('community-member/', CommunityMemberSignupView.as_view(), name='register-community-member'),
    path('medical-personel-registration/', MedicalPersonellSignupView.as_view(), name='register-medical-personell'),
    path('activate/', VerifyEmail,name="email-verify"),
]
