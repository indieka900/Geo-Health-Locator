from django.shortcuts import render,redirect
from django.views.generic import CreateView
from geo_health_app.forms import ReportDiseaseForm, OrderAmbulanceForm
from geo_health_app.models import Disease, Patient


def home(request):
    return render(request, 'index.html')

def order_ambulance(request):
    pass

def report_disease(request):
    pass

class ReportDiseaseView(CreateView):
    model = Disease
    form_class = ReportDiseaseForm
    template_name = "report_disease.html"

    def form_valid(self, form):
        if form.is_valid():
            symptoms = form.cleaned_data.get('symptoms')
            latitude = form.cleaned_data.get('latitude')
            longitude = form.cleaned_data.get('longitude')
            disease = Disease(symptoms=symptoms, latitude=latitude,longitude=longitude)
            
            disease.save()
            disease.reporter.set([self.request.user])
            return redirect('/')


class OrderAmbulanceView(CreateView):
    model = Patient
    form_class = OrderAmbulanceForm
    template_name = "order_ambu.html"

    def form_valid(self, form):
        if form.is_valid():
            
            
            # user = form.save(commit=False)
            # user.role = "customer"
            # user.save()
            pass

        return render(self.request, "accounts/sign_alert.html")


# Create your views here.
