from django import forms

from .models import Account


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
        """
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "Las contraseñas no coinciden"
            )