from django import forms
from .models import User, MedicalPersonel  # Import the required models

class UserSignUpForm(forms.ModelForm):
    email = forms.EmailField(max_length=156, required=True)
    phone = forms.CharField(max_length=20, required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
    class Meta:
        model = User
        fields = ("username", "first_name", "middle_name", "last_name", "identification",
                  "gender", "phone", "email", "county", "sub_county", "ward", "location",
                  "sub_location", "village")

    password1 = forms.CharField(
        label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password Confirmation",
        widget=forms.PasswordInput)

    

    

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match!")

        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = False
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()

        return user

class MedicalPersonnelSignUpForm(UserSignUpForm):
    kmdb_number = forms.CharField(
        label="KMDB Number",
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Enter KMDB Number','class':'form-control'}),
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Set the default role to "Medical Personnel"
        self.fields['kmdb_number'].required = True 
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = User
        fields = ("username", "first_name", "middle_name", "last_name", "identification",
                  "gender", "phone", "email", "county", "sub_county", "ward", "location",
                  "sub_location", "village")

        
    def save(self, commit=True):
        user = super(UserSignUpForm, self).save(commit=False)
        user.is_active = False
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()

        kmdb_number = self.cleaned_data.get('kmdb_number')
        medical_personnel = MedicalPersonel(user=user, kmdb_number=kmdb_number)
        if commit:
            medical_personnel.save()

        return user
