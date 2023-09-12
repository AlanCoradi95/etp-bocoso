from django import forms
from .models import NivEducativo

class NivelForm(forms.ModelForm):
    class Meta:
        model = NivEducativo

        fields = [
            'nombre'
        ]