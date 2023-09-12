from django import forms
from .models import Inscripcion
from apps.niveducativos.models import NivEducativo
class CrearInscripcionForm(forms.ModelForm):
    #niveducativo = NivEducativo.objects.all() #forms.ModelChoiceField(queryset=NivEducativo.objects.all())

    class Meta:
        model = Inscripcion
        fields = [
            'nombre',
            'apellido',
            'dni',
            'telefono',
            'direccion',
            'email',
            'niveducativo',
        ]