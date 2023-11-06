from accounts.models import User, Administrator, MedicalPersonel, CommunityMember

from django import forms

from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class CustomUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'required': '',
            'type': 'text',
            'placeholder': 'Johndoe',
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'required': '',
            'type': 'email',
            'placeholder': 'Johndoe@mail.com',
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'required': '',
            'type': 'password',
            'placeholder': 'password',
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'required': '',
            'type': 'password',
            'placeholder': 'password',
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'required': '',
            'type': 'password',
            'placeholder': 'password',
        })
        self.fields['age'].widget.attrs.update({
            'class': 'form-control',
            'required': '',
            'type': 'password',
            'placeholder': 'Age',
        })

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'age', 'password1', 'password2']


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = UserChangeForm.Meta.fields
