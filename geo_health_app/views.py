from django.shortcuts import render,redirect
from django.views.generic import CreateView,ListView
from geo_health_app.forms import ReportDiseaseForm, OrderAmbulanceForm, TreatPatientForm
from geo_health_app.models import Disease, Patient, TreatPatient
from django.db.models import Q
from accounts.models import Hospital,MedicalPersonel
from accounts.decorators import medical_personell_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


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

@login_required(login_url='/')
class OrderAmbulanceView(CreateView):
    model = Patient
    form_class = OrderAmbulanceForm
    template_name = "order_ambu.html"
    
    def get_initial(self):
        initial = super().get_initial()
        initial['type_l'] = 'Ambulance'
        return initial

    def form_valid(self, form):
        latitude = form.cleaned_data.get('latitude')
        longitude = form.cleaned_data.get('longitude')
        if form.is_valid():
            form.latitude = latitude
            form.longitude = longitude
            form.save()
            return redirect('/hospitals/')

        return render(self.request, "accounts/sign_alert.html")

@medical_personell_required
def hospital_dash(request):
    user = request.user
    medic = MedicalPersonel.objects.get(user=user)
    doctors = MedicalPersonel.objects.filter(hospital=medic.hospital)
    diseases = Disease.objects.filter(reported_to = medic.hospital.hospital_name)
    ambu = Patient.objects.filter(reported_to = medic.hospital.hospital_name, type_l='Ambulance')
    patients = TreatPatient.objects.filter(reported_to = medic.hospital.hospital_name).order_by('-reported_at')
    disease = len(diseases)
    
    context = {
        "nav":"dash",
        "doctors":doctors,
        "ambu":ambu,
        "patients":patients,
        "dis":disease,
    }
    return render(request, 'hospital/index.html',context)

    
@medical_personell_required
def lab_test(request):
    user = request.user
    medic = MedicalPersonel.objects.get(user=user)
    tests = TreatPatient.objects.filter(reported_to = medic.hospital.hospital_name,lab_test_results__isnull=True,)
    context= {
        "nav":"Lab",
        'tests':tests,
    }
    return render(request, 'lab_dashboard.html',context)

@medical_personell_required
def tests(request):
    user = request.user
    medic = MedicalPersonel.objects.get(user=user)
    tests = TreatPatient.objects.filter(reported_to = medic.hospital.hospital_name,lab_test_results__isnull=False,)
    context= {
        "nav":"test",
        'tests':tests,
        'doc':'doc',
    }
    return render(request, 'lab_dashboard.html',context)

@medical_personell_required
def result(request, id):
    treat = TreatPatient.objects.get(id=id)
    if request.method == 'POST':
        results = request.POST.get('results')
        treat.lab_test_results =results
        treat.save()
        return redirect('/tests/')
    return render(request, 'result.html',{'action':'lab','id':id})

@medical_personell_required
def result_D(request, id):
    treat = TreatPatient.objects.get(id=id)
    if request.method == 'POST':
        drugs = request.POST.get('drugs')
        treat.drug_prescription = drugs
        treat.save()
        return redirect('/tests/')
    return render(request, 'result.html', {'action':'drug','id':id})

@medical_personell_required
def reported_diseases(request):
    user = request.user
    medic = MedicalPersonel.objects.get(user=user)
    diseases = Patient.objects.filter(reported_to = medic.hospital.hospital_name, type_l='Disease').order_by('-reported_at')
    context = {
        'diseases':diseases,
        'nav' : 'report'
    }
    return render(request, 'diseases.html', context)

@medical_personell_required
def ambulances(request):
    user = request.user
    medic = MedicalPersonel.objects.get(user=user)
    diseases = Patient.objects.filter(reported_to = medic.hospital.hospital_name, type_l='Ambulance').order_by('-reported_at')
    context = {
        'diseases':diseases,
        'nav' : 'ambu'
    }
    return render(request, 'diseases.html', context)
    

class TreatPatientView(CreateView):
    model = TreatPatient
    form_class = TreatPatientForm
    template_name = "treatpatient.html"
    
    @method_decorator(medical_personell_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nav'] = 'treat_p'
        return context
    
    
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
                treatment = TreatPatient(full_name=full_name, op_number=op_number, age=age, height=height, 
                                        bp_reading=bp_reading, glucose_level=glucose_level, weight_reading=weight_reading,
                                        temperature_reading=temperature_reading, symptoms=symptoms,
                                        prescribe_lab_test=prescribe_lab_test
                                        )
                
                treatment.save()
                return redirect('/dashboard/')
            else:
                return render(request, self.template_name, {'form': form,'nav':'treat_p'})
        else:
            return render(request, self.template_name, {'form': form,'nav':'treat_p'})