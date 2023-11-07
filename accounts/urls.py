from django.urls import path
from accounts.views import AdministratorSignupView, CommunityMemberSignupView

app_name = 'accounts'

urlpatterns = [
    path('community-member/', CommunityMemberSignupView.as_view(), name='register-community-member'),
    path('admin-reqistration/', AdministratorSignupView.as_view(), name='register-admin'),
]
