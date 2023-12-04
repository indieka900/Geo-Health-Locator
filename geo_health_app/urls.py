from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('',views.home, name='home'),
    path('order-ambulance/<int:id>/',views.OrderAmbulanceView.as_view(), name='order-ambulance'),
    path('hospitals/', views.HospitalListView.as_view(), name='hospital_list'),
    path('report-disease/<int:id>/', views.ReportDiseaseView.as_view(), name='report_disease'),
    path('dashboard/', views.hospital_dash, name='dashboard'),
    path('tests/', views.lab_test, name='tests'),
    path('lists/', views.tests, name='lists'),
    path('diseases/', views.reported_diseases, name='diseases'),
    path('treat-patient/', views.TreatPatientView.as_view(), name="treat_patient"),
    path('results/<int:id>/', views.result, name='results'),
    
]
