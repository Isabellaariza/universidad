from django import forms
from .models import Entidades
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EntidadesForm(forms.ModelForm):
    class Meta:
        model = Entidades
        fields = '__all__'

class RegistroEntidadForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']