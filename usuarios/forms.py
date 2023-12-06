from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from usuarios.models import User

class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Contraseña'}))
    password2 = forms.CharField(label='Confirmación de contraseña', widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Confirmación de contraseña'}))

    class Meta:
        model = User
        fields = ['username', 'last_name', 'email', 'phone_number']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        fields_to_add_class = ['last_name', 'email', 'phone_number']

        self.fields['username'].widget.attrs['class'] = 'form-input'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
        self.fields['last_name'].widget.attrs['class'] = 'form-input'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Apellido'
        self.fields['email'].widget.attrs['class'] = 'form-input'
        self.fields['email'].widget.attrs['placeholder'] = 'Dirección de correo electrónico'
        self.fields['phone_number'].widget.attrs['class'] = 'form-input'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Número de teléfono'

        for field_name in ['password1', 'password2']:
            self.fields[field_name].widget.attrs['class'] = 'form-input'

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Dirección de correo electrónico'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Contraseña'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-input'
