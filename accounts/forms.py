from django import forms
from .models import User, Administrator, CommunityMember, MedicalPersonel, Profile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'middle_name', 'last_name', 'identification', 'email', 'gender', 'phone', 'role']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'identification': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
        }

class AdministratorForm(forms.ModelForm):
    class Meta:
        model = Administrator
        fields = ['user', 'first_name', 'middle_name', 'last_name', 'county', 'sub_county']

class CommunityMemberForm(forms.ModelForm):
    class Meta:
        model = CommunityMember
        fields = ['user', 'county', 'sub_county', 'ward', 'location', 'village']

class MedicalPersonelForm(forms.ModelForm):
    class Meta:
        model = MedicalPersonel
        fields = ['user', 'kmdb_number', 'email']

