from django.urls import path
from accounts.views import MedicalPersonellSignupView, Medicalpersonellogin, CommunityMemberSignupView,activate, Communitymemberlogin

app_name = 'accounts'

urlpatterns = [
    path('community-member/', CommunityMemberSignupView.as_view(), name='register-community-member'),
    path('medical-personel-registration/', MedicalPersonellSignupView.as_view(), name='register-medical-personell'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',  
        activate, name='activate'),
    path('member-login/', Communitymemberlogin,name="login-member"),
    path('medics-login/', Medicalpersonellogin,name="login-medics"),
]
