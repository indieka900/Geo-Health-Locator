import datetime
from accounts.decorators import administrator_required, community_member_required, medical_personell_required
from accounts.forms import (MedicalPersonnelSignUpForm,UserSignUpForm,)
from .tokens import account_activation_token 
from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes, force_str  
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string 
from accounts.models import Administrator, CommunityMember, User, MedicalPersonel
from accounts.sendMails import  send_password_reset_email
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import never_cache
from django.views.generic import CreateView
from django.conf import settings
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .forms import UserSignUpForm

decorators = [never_cache, login_required, administrator_required]


# @method_decorator(decorators, name='dispatch')


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
            current_site = get_current_site(self.request)  
            mail_subject = 'Verify your account'  
            message = render_to_string('acc_active.html', {  
                'user': user,  
                'domain': current_site.domain,  
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
                'token':account_activation_token.make_token(user),  
            })  
            to_email = form.cleaned_data.get('email')  
            email = EmailMessage(  
                        mail_subject, message, to=[to_email]  
            )  
            email.send()

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
            current_site = get_current_site(self.request)  
            mail_subject = 'Verify your account'  
            message = render_to_string('acc_active.html', {  
                'user': user,  
                'time': datetime.date.today().year,
                'domain': current_site.domain,  
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
                'token':account_activation_token.make_token(user),  
            })  
            to_email = form.cleaned_data.get('email')  
            email = EmailMessage(  
                        mail_subject, message, to=[to_email]  
            )  
            email.send()
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
            if member.is_active:
                login(request, member)
                messages.success(request, 'Logged in succesfully')
                return redirect('/hospitals/')
            else:
                messages.error(request, 'Please activate your account')
                return redirect('/') 
        else:
            messages.error(request, 'email or password does not exist')
            return redirect('/')
    return render(request,'login.html',{'member':'member'})


def Medicalpersonellogin(request):
    
    # if request.user.is_authenticated:
    #     return redirect('/')
    if request.method == 'POST':
        kmdb_number = request.POST.get('kmdb_number')
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            medics = MedicalPersonel.objects.get(kmdb_number=kmdb_number)
        except MedicalPersonel.DoesNotExist:
            messages.error(request, 'KMDB number does not exist!')
            return redirect('/')
        if medics.user.email == email:
            user = authenticate(request, email=email, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'Logged in successfully')
                    return redirect('/dashboard/')
                else:
                    messages.error(request, 'Please activate your account')
                    return redirect('/')
            else:
                messages.error(request, 'Invalid password')
                return redirect('/')
        else:
            messages.error(request, 'Email does not match')
            return redirect('/')
    return render(request,'login.html',{'medics':'medics'})

#logout the logged in user   
def log_out(request):
    logout(request)
    return redirect('/')

def RequestPasswordReset(request):
    context = {
        # Add context data as needed
    }
    return render(request, "accounts/RequestPasswordReset.html", context)



def activate(request, uidb64, token):  
    User = get_user_model()  
    try:  
        uid = force_str(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()  
        messages.success(request,"Account was Successfully Verified.")
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')  
    else:  
        return HttpResponse('Activation link is invalid!')