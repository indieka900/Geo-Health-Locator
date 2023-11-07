from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('',views.home, name='home'),
    # path('community-member/login/',views.communityMember, name='community-login'),
    # path('community-member/register/',views.communityMemberRegister, name='community-register'),
    
]
