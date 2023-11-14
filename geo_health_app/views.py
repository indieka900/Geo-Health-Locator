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
            # name = form.cleaned_data.get('name')
            longitude = self.request.POST.get('longitude')
            latitude = self.request.POST.get('latitude')
            # symptoms = form.cleaned_data.get('symptoms')
            print(latitude)
            pass
            # disease = Disease(reporter = self.request.user,latitude=latitude, longitude=longitude)
            # disease.save()
            # return redirect('/')

        return render(self.request, "accounts/sign_alert.html")

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
