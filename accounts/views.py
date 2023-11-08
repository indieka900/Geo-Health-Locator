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
import jwt
# from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework_simplejwt.views import (TokenObtainPairView,
#                                             TokenRefreshView)

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