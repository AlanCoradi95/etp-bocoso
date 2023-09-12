from django import forms
from .models import Comentario

class CrearComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = [
            'titulo',
            'descripcion'
        ]