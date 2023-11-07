from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm, AdministratorForm, CommunityMemberForm, MedicalPersonelForm

def create_user(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            # You can add any additional processing or redirection here.
            return redirect('/')
    else:
        user_form = UserForm()
    
    return render(request, 'usercreationform.html', {'user_form': user_form})

def create_administrator(request):
    if request.method == 'POST':
        admin_form = AdministratorForm(request.POST)
        if admin_form.is_valid():
            administrator = admin_form.save()
            # You can add any additional processing or redirection here.
            return redirect('administrator_created')
    else:
        admin_form = AdministratorForm()
    
    return render(request, 'create_administrator.html', {'admin_form': admin_form})

def create_community_member(request):
    if request.method == 'POST':
        member_form = MedicalPersonelForm(request.POST)
        if member_form.is_valid():
            community_member = member_form.save()
            # You can add any additional processing or redirection here.
            return redirect('/')
    else:
        member_form = MedicalPersonelForm()
    
    return render(request, 'communityRegister.html', {'member_form': member_form})

def create_medical_personel(request):
    if request.method == 'POST':
        medical_form = MedicalPersonelForm(request.POST)
        if medical_form.is_valid():
            medical_personel = medical_form.save()
            # You can add any additional processing or redirection here.
            return redirect('/')
    else:
        medical_form = MedicalPersonelForm()
    
    return render(request, 'create_medical_personel.html', {'medical_form': medical_form})

