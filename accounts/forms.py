from django import forms
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError

from .models import Account, UserProfile


class RegistrationForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Ingrese su contraseña'
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirme su contraseña'
    }))

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs["placeholder"] = "Ingrese su nombre"
        self.fields["last_name"].widget.attrs["placeholder"] = "Ingrese su apellido"
        self.fields["phone_number"].widget.attrs["placeholder"] = "Ingrese su número de teléfono"
        self.fields["email"].widget.attrs["placeholder"] = "Ingrese su correo electrónico"
        
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def clean(self):
        """
        Verify that the two password entries match
        and the password is at least 8 chars long
        """
        cleaned_data = super(RegistrationForm, self).clean()  
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if len(password) < 8:
            raise forms.ValidationError(
                "La contraseña debe tener al menos 8 caracteres"
            )

        if password != confirm_password:
            raise forms.ValidationError(
                "Las contraseñas no coinciden"
            )
        
        return cleaned_data 
    
    def clean_email(self):
        """ 
        Verify that the email is not already registered
        """
        email = self.cleaned_data.get('email')
        if Account.objects.filter(email=email).exists():
            raise forms.ValidationError("El correo ingresado ya esta en uso")
        return email
    

class UserForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'phone_number')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

class UserProfileForm(forms.ModelForm):
    profile_picture = forms.ImageField(required=False, error_messages = {'invalid':("Image files only")}, widget=forms.FileInput)
    class Meta:
        model = UserProfile
        fields = ('address_line_1', 'city', 'comuna', 'profile_picture')

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'