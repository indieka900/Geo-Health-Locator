from django.shortcuts import render,redirect
from django.views.generic import CreateView,ListView
from geo_health_app.forms import ReportDiseaseForm, OrderAmbulanceForm, TreatPatientForm
from geo_health_app.models import Disease, Patient, TreatPatient
from accounts.models import Hospital,MedicalPersonel


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

def hospital_dash(request):
    
    return render(request, 'hospital/index.html')
    


class TreatPatientView(CreateView):
    model = TreatPatient
    form_class = TreatPatientForm
    template_name = "treatpatient.html"

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        # hospital = Hospital.objects.get(id=id)
        form = self.form_class(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data.get('full_name')
            op_number = form.cleaned_data.get('op_number')
            age = form.cleaned_data.get('age')
            height = form.cleaned_data.get('height')
            bp_reading = form.cleaned_data.get('bp_reading')
            glucose_level = form.cleaned_data.get('glucose_level')
            weight_reading = form.cleaned_data.get('weight_reading')
            temperature_reading = form.cleaned_data.get('temperature_reading')
            symptoms = form.cleaned_data.get('symptoms')
            prescribe_lab_test = form.cleaned_data.get('prescribe_lab_test')

            med = MedicalPersonel.objects.get(user=request.user)
            if med:
                kmdb_no = med.kmdb_number
                treatment = TreatPatient(full_name=full_name, op_number=op_number, age=age, height=height, 
                                        bp_reading=bp_reading, glucose_level=glucose_level, weight_reading=weight_reading,
                                        temperature_reading=temperature_reading, symptoms=symptoms,
                                        prescribe_lab_test=prescribe_lab_test, kmdb_no=kmdb_no,
                                        # reported_to= hospital.hospital_name
                                        )
                
                treatment.save()
                return redirect('/')
            else:
                return render(request, self.template_name, {'form': form})
        else:
            return render(request, self.template_name, {'form': form})