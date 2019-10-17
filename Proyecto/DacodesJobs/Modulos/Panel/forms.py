from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {
            'username' : 'Nombre de usuario',
            'first_name' : 'Nombres',
            'last_name' : 'Apellidos',
            'email' : 'Correo'
        }
