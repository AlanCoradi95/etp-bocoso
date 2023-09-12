from django import forms
from .models import Noticia

class CrearNoticiaForm(forms.ModelForm):

    class Meta:
        model = Noticia
        fields = [
            'titulo',
            'descripcion',
            'portada'
        ]
