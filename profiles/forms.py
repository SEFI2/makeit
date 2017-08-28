from django import forms
from django.contrib.auth.models import User
from .models import Profile


class SignUpForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control'}),
        max_length=30,
        required=True
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control'}),
        required=True
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control'}),
        label="Confirm your password",
        required=True
    )

    class Meta:
        model = User
        fields = ['username' , 'password' , 'confirm_password']


class UpdateProfileForm(forms.ModelForm):
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class':'form-control'}),
        max_length=50
    )
    surname = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=50
    )
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=50
    )
    skills = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True,
        max_length=100
    )

    class Meta:
        model = Profile
        fields = ['name' , 'surname' , 'email' , 'skills' , 'avatar']


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control'}),
        max_length=30,
        required=True
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control'})
    )

    class Meta:
        model = User
        fields = ['username' , 'password']

