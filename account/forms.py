from django import forms

from .models import UserBase
from django.contrib.auth.forms import (AuthenticationForm)

class UserLoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Username', 'id': 'login-username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'id': 'login-pwd',
        }
    ))


class RegistrationForm(forms.ModelForm):

    user_name = forms.CharField(label='Nombre de Usuario', min_length=4, max_length=50, help_text='Required')
    email     = forms.EmailField(max_length=100, help_text='Required', error_messages={'required': 'Lo sentimos, necesitas un correo electronico'})
    password  = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repite Contraseña', widget=forms.PasswordInput)

    class Meta:
        model  = UserBase
        fields = ('user_name', 'email')

    def clean_user_name(self): 
        user_name = self.cleaned_data['user_name'].lower()
        r = UserBase.objects.filter(user_name=user_name)
        if r.count():
            raise forms.ValidationError("El nombre de usuario ya existe")
        return user_name
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return cd['password2']

    def clean_email(self): 
        email = self.cleaned_data['email']
        if UserBase.objects.filter(email=email).exists():
            raise forms.ValidationError("El correo ya existe")
        return email
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].widget.attrs.update(
            {'class': 'form-control mb-4', 'placeholder': 'Nombre de Usuario'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-4', 'placeholder': 'Correo Electronico'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control mb-4', 'placeholder': 'Contraseña'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control mb-4', 'placeholder': 'Repite Contraseña'})
        