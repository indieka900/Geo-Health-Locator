# from django import forms
# from .models import User, Profile

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'middle_name', 'last_name', 'identification', 'email', 'gender', 'phone', 'role']
#         widgets = {
#             'username': forms.TextInput(attrs={'class': 'form-control'}),
#             'first_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'last_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'identification': forms.NumberInput(attrs={'class': 'form-control'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control'}),
#             'gender': forms.Select(attrs={'class': 'form-control'}),
#             'phone': forms.TextInput(attrs={'class': 'form-control'}),
#             'role': forms.Select(attrs={'class': 'form-control'}),
#         }

# class AdministratorForm(forms.ModelForm):
#     class Meta:
#         model = Administrator
#         fields = ['user', 'first_name', 'middle_name', 'last_name', 'county', 'sub_county']

# class CommunityMemberForm(forms.ModelForm):
#     class Meta:
#         model = CommunityMember
#         fields = ['user', 'county', 'sub_county', 'ward', 'location', 'village']

# class MedicalPersonelForm(forms.ModelForm):
#     class Meta:
#         model = MedicalPersonel
#         fields = ['user', 'kmdb_number', 'email']


from django import forms
from accounts.models import User, Administrator, CommunityMember, MedicalPersonel
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.db import transaction
from django.forms import ModelForm


# User Creation Form in the Django Admin
class UserCreationForm(ModelForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "middle_name", "last_name", "identification",
                  "gender", "phone", "email", "county", "sub_county", "ward", "location",
                  "sub_location", "village")

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password Confirmation", widget=forms.PasswordInput)

    def cleaned_password(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don\'t match.")

        return password2

    def save(self, commit=False):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()

        return user

    # User Change form for the django Admin Panel


class UserChangeForm(ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ("username", "first_name", "middle_name", "last_name", 
                  "phone", "is_active", "is_admin",
                  "is_staff")

    def cleaned_password(self):
        return self.initial["password"]


class UserSignUpForm(ModelForm):
    email = forms.EmailField(max_length=156, required=True)
    phone = forms.CharField(max_length=20, required=True)

    class Meta:
        model = User
        fields = ('username', "phone", 'email')

    password1 = forms.CharField(
        label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password Confirmation",
        widget=forms.PasswordInput)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Password don\'t match!')

        return password2

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = False
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()

        return user


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "middle_name", "last_name", "phone",)


class CommunityMemberProfileUpdateForm(forms.ModelForm):
    bio = forms.CharField(label="Bio", widget=forms.Textarea(
        attrs={"class": "form-control", "placeholder": "",
               'rows': "3", "cols": '50'}))

    class Meta:
        model = CommunityMember
        fields = ( "profile_picture",
                  "bio",)


class AdministratorProfileUpdate(forms.ModelForm):
    bio = forms.CharField(label="Bio", widget=forms.Textarea(
        attrs={"class": "form-control", "placeholder": "",
               'rows': "3", "cols": '50'}))

    class Meta:
        model = Administrator
        fields = ("profile_picture", "bio")

class MedicalPersonelProfileUpdateForm(forms.ModelForm):
    bio = forms.CharField(label="Bio", widget=forms.Textarea(
        attrs={"class": "form-control", "placeholder": "",
               'rows': "3", "cols": '50'}))

    class Meta:
        model = MedicalPersonel
        fields = ( "profile_picture",
                  "bio", "kmdb_number")