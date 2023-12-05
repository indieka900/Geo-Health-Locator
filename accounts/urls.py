from django.urls import path
from accounts.views import (MedicalPersonellSignupView, Medicalpersonellogin, 
                            CommunityMemberSignupView,activate, log_out,
                            Communitymemberlogin)

app_name = 'accounts'

urlpatterns = [
    path('community-member/', CommunityMemberSignupView.as_view(), name='register-community-member'),
    path('medical-personel-registration/', MedicalPersonellSignupView.as_view(), name='register-medical-personell'),
    path('activate/<str:uidb64>/<str:token>/', activate, name='activate'),
    path('member-login/', Communitymemberlogin,name="login-member"),
    path('medics-login/', Medicalpersonellogin,name="login-medics"),
    path('logout/', log_out, name="logout"),
]
