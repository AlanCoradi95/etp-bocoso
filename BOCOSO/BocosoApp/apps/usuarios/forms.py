from django import forms
from .models import Usuario
#from apps.roles.models import Rol
from django.contrib.auth.forms import UserCreationForm

class UsuarioForm(UserCreationForm):
    first_name= forms.CharField
    last_name= forms.CharField
    #rol = forms.ModelChoiceField(queryset=Rol.objects.all()) --> lo comentamos para que no se puedan registrar usuarios con roles no autorizados
    
    class Meta:
        model = Usuario
        fields = ['first_name','last_name','email','username','password1','password2']

class EditaRol(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['rol']

class EditarUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['first_name','last_name','email','foto']