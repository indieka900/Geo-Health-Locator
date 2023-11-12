from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('',views.home, name='home'),
    path('report-disease/',views.ReportDiseaseView.as_view(), name='report-disease'),
    path('order-ambulance/',views.OrderAmbulanceView.as_view(), name='order-ambulance'),
    # path('community-member/register/',views.communityMemberRegister, name='community-register'),
    
]
