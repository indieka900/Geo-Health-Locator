from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('community-member/login/',views.communityMember, name='community-login'),
    path('community-member/register/',views.communityMemberRegister, name='community-register'),
    
]
