from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('',views.home, name='home'),
    path('order-ambulance/<int:id>/',views.OrderAmbulanceView.as_view(), name='order-ambulance'),
    path('hospitals/', views.HospitalListView.as_view(), name='hospital_list'),
    path('report-disease/<int:id>/', views.ReportDiseaseView.as_view(), name='report_disease'),
    # path('community-member/register/',views.communityMemberRegister, name='community-register'),
    
]
