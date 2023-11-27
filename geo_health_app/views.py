from django.shortcuts import render,redirect
from django.views.generic import CreateView,ListView
from geo_health_app.forms import ReportDiseaseForm, OrderAmbulanceForm
from geo_health_app.models import Disease, Patient
from accounts.models import Hospital


def home(request):
    return render(request, 'index.html')


class ReportDiseaseView(CreateView):
    model = Disease
    form_class = ReportDiseaseForm
    template_name = "repo_disease.html"

    def post(self, request,id, *args, **kwargs):
        form = self.form_class(request.POST)
        hospital = Hospital.objects.get(id=id)
        form = self.form_class(request.POST)
        if form.is_valid():
            symptoms = form.cleaned_data.get('symptoms')
            latitude = form.cleaned_data.get('latitude')
            longitude = form.cleaned_data.get('longitude')
            disease = Disease(symptoms=symptoms, latitude=latitude, longitude=longitude, reported_to= hospital.hospital_name)
            
            disease.save()
            disease.reporter.set([request.user])
            return redirect('/')
        else:
            return render(request, self.template_name, {'form': form})

class HospitalListView(ListView):
    model = Hospital
    template_name = "choose_hospital.html"
    context_object_name = 'hospitals'

class OrderAmbulanceView(CreateView):
    model = Patient
    form_class = OrderAmbulanceForm
    template_name = "order_ambu.html"

    def form_valid(self, form,id):
        if form.is_valid():
            
            
            # user = form.save(commit=False)
            # user.role = "customer"
            # user.save()
            pass

        return render(self.request, "accounts/sign_alert.html")


# Create your views here.
