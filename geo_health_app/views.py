from django.shortcuts import render,redirect
from django.views.generic import CreateView,ListView
from geo_health_app.forms import ReportDiseaseForm, OrderAmbulanceForm
from geo_health_app.models import Disease, Patient
from accounts.models import Hospital


def home(request):
    return render(request, 'index.html')


class ReportDiseaseView(ListView):
    model = Disease
    form_class = ReportDiseaseForm
    template_name = "report_disease.html"
    queryset = Hospital.objects.all()
    context_object_name = 'hospitals'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            # Handle the case where the form is not valid
            return self.form_invalid(form)

    def form_valid(self, form):
        symptoms = form.cleaned_data.get('symptoms')
        latitude = form.cleaned_data.get('latitude')
        longitude = form.cleaned_data.get('longitude')
        disease = Disease(symptoms=symptoms, latitude=latitude, longitude=longitude)
        
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
