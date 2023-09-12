from django import forms
from .models import Aspirante

class CrearAspiranteForm(forms.ModelForm):
    class Meta:
        model = Aspirante
        fields = [
            'nombre',
            'apellido',
            'telefono',
            'email',
            'comentario',
            'cv'
        ]