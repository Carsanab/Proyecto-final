from django import forms 

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class registroformulario(UserCreationForm):

    first_name=forms.CharField(label="Nombre")
    last_name=forms.CharField(label="Apellido")
    email=forms.EmailField(label="Correo")
    password1=forms.CharField(label="Contraseña",widget=forms.PasswordInput)
    password2=forms.CharField(label="Repetir Contraseña",widget=forms.PasswordInput)

    class Meta:

        model = User
        fields=["username",'first_name','last_name','email','password1','password2']