# from django.shortcuts import render, redirect
# from .models import User
# from .forms import UserForm

# def create_user(request):
#     if request.method == 'POST':
#         user_form = UserForm(request.POST)
#         if user_form.is_valid():
#             user = user_form.save()
#             # You can add any additional processing or redirection here.
#             return redirect('/')
#     else:
#         user_form = UserForm()
    
#     return render(request, 'usercreationform.html', {'user_form': user_form})

# def create_administrator(request):
#     if request.method == 'POST':
#         admin_form = AdministratorForm(request.POST)
#         if admin_form.is_valid():
#             administrator = admin_form.save()
#             # You can add any additional processing or redirection here.
#             return redirect('administrator_created')
#     else:
#         admin_form = AdministratorForm()
    
#     return render(request, 'create_administrator.html', {'admin_form': admin_form})

# def create_community_member(request):
#     if request.method == 'POST':
#         member_form = MedicalPersonelForm(request.POST)
#         if member_form.is_valid():
#             community_member = member_form.save()
#             # You can add any additional processing or redirection here.
#             return redirect('/')
#     else:
#         member_form = MedicalPersonelForm()
    
#     return render(request, 'communityRegister.html', {'member_form': member_form})

# def create_medical_personel(request):
#     if request.method == 'POST':
#         medical_form = MedicalPersonelForm(request.POST)
#         if medical_form.is_valid():
#             medical_personel = medical_form.save()
#             # You can add any additional processing or redirection here.
#             return redirect('/')
#     else:
#         medical_form = MedicalPersonelForm()
    
#     return render(request, 'create_medical_personel.html', {'medical_form': medical_form})

from accounts.decorators import administrator_required, community_member_required
from accounts.forms import (MedicalPersonnelSignUpForm,
                            UserSignUpForm,
                            )
from accounts.models import Administrator, CommunityMember, User, MedicalPersonel
from accounts.sendMails import send_activation_mail, send_password_reset_email
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.generic import CreateView
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


decorators = [never_cache, login_required, administrator_required]


# @method_decorator(decorators, name='dispatch')
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .forms import UserSignUpForm

class MedicalPersonellSignupView(CreateView):
    model = User
    form_class = MedicalPersonnelSignUpForm
    template_name = "usercreationform.html"

    def get_context_data(self, **kwargs):
        kwargs["user_type"] = "Medical Personel"
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        if form.is_valid():
            user = form.save(commit=False)
            user.role = "Medical Personel"
            user.save()
            kmdb_number = form.cleaned_data.get('kmdb_number')
            medical_personnel = MedicalPersonel(user=user, kmdb_number=kmdb_number)
            medical_personnel.save()
            send_activation_mail(user, self.request)

        return render(self.request, "sign_alert.html")

class CommunityMemberSignupView(CreateView):
    model = User
    form_class = UserSignUpForm
    template_name = "usercreationform.html"

    def get_context_data(self, **kwargs):
        kwargs["user_type"] = "Community Member"
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        if form.is_valid():
            user = form.save(commit=False)
            user.role = "Community Member"
            user.save()
            community_member = CommunityMember(user=user)
            community_member.save()
            send_activation_mail(user, self.request)
        return render(self.request, "sign_alert.html")

def Communitymemberlogin(request):
    
    # if request.user.is_authenticated:
    #     return redirect('/')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            member= CommunityMember.objects.get(user__email=email)
        except CommunityMember.DoesNotExist:
            messages.error(request, 'email does not exist!') 
        
        member = authenticate(request, email=email, password=password)
        
        if member is not None:
            login(request, member)
            messages.success(request, 'Logged in succesfully')
            return redirect('/')
        else:
            messages.error(request, 'email or password does not exist')
            return redirect('/login')
    return render(request,'login.html',{'member':'member'})


def Medicalpersonellogin(request):
    
    # if request.user.is_authenticated:
    #     return redirect('/')
    if request.method == 'POST':
        kmdb_mumber = request.POST.get('kmdb_mumber')
        password = request.POST.get('password')
        try:
            medics= MedicalPersonel.objects.get(kmdb_mumber=kmdb_mumber)
        except MedicalPersonel.DoesNotExist:
            messages.error(request, 'email does not exist!') 
        
        medics = authenticate(request, kmdb_mumber=kmdb_mumber, password=password)
        
        if medics is not None:
            login(request, medics)
            messages.success(request, 'Logged in succesfully')
            return redirect('/')
        else:
            messages.error(request, 'email or password does not exist')
            return redirect('/login')
    
    return render(request,'login.html',{'medics':'medics'})



def RequestPasswordReset(request):
    context = {
        # Add context data as needed
    }
    return render(request, "accounts/RequestPasswordReset.html", context)


def VerifyEmail(request):
    token = request.GET.get("token")
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms="HS256"
        )
        user = User.objects.get(id=payload['user_id'])
        if not user.is_active:
            user.is_active = True
            user.save()
            messages.success(request,
                             "Account was Successfully Verified.")
        else:
            messages.info(request,
                          """Your Account has already been activated.
                          You can now login and 
                          place your order today.
                        """)
    except jwt.ExpiredSignatureError as identifier:
        messages.warning(request,
                         "The Activation Link Expired!")
    except jwt.exceptions.DecodeError as identifier:
        messages.warning(request, "Invalid Activation Link!")
    context = {
    }
    return render(request, "verify.html", context)