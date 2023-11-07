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
from accounts.forms import (AdministratorProfileUpdate,
                            CommunityMemberProfileUpdateForm, UserSignUpForm,
                            UserUpdateForm)
from accounts.models import Administrator, CommunityMember, User, MedicalPersonel
from accounts.sendMails import send_activation_mail, send_password_reset_email
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.generic import CreateView

decorators = [never_cache, login_required, administrator_required]


# @method_decorator(decorators, name='dispatch')
class AdministratorSignupView(CreateView):
    model = User
    form_class = UserSignUpForm
    template_name = "accounts/adminSignup.html"

    def get_context_data(self, **kwargs):
        kwargs["user_type"] = "Admin"
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        if form.is_valid():
            user = form.save(commit=False)
            user.is_admin = True
            user.is_staff = True
            user.role = "administrator"
            user.save()
            send_activation_mail(user, self.request)

        return render(self.request, "accounts/sign_alert.html")


class CommunityMemberSignupView(CreateView):
    model = User
    form_class = UserSignUpForm
    template_name = "accounts/customerSignup.html"

    def get_context_data(self, **kwargs):
        kwargs["user_type"] = "Customer"
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        if form.is_valid():
            user = form.save(commit=False)
            user.role = "customer"
            user.save()

            send_activation_mail(user, self.request)
        return render(self.request, "accounts/sign_alert.html")


def RequestPasswordReset(request):
    context = {

    }
    return render(request, "accounts/RequestPasswordReset.html", context)