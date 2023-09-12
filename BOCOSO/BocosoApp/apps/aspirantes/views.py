from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import CreateView
from .models import Aspirante
from .forms import CrearAspiranteForm
# Create your views here.
class CrearAspirantes(CreateView):
    model = Aspirante
    template_name='aspirantes/aplicar.html'
    form_class = CrearAspiranteForm
   
    def get_success_url(self):
        return reverse('index')

def listaAplicantes(request):
    template_name = 'aspirantes/listaaspirantes.html'
    aspirantes = Aspirante.objects.all()
    contexto = {
        'aspirantes':aspirantes
    }

    return render(request,template_name,contexto)