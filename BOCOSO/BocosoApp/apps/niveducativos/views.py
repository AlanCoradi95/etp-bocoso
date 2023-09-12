from django.shortcuts import render
from django.urls import reverse
from .models import NivEducativo
from .forms import NivelForm
from utils.mixins import ABM,ABMMixin
from django.views.generic.edit import DeleteView,CreateView
# Create your views here.
@ABM()
def listaNiveducativos(request):
    template_name = 'niveducativos/niveducativos.html'
    niveducativos = NivEducativo.objects.all()

    contexto = {
        'niveducativos' : niveducativos
    }

    return render(request,template_name,contexto)

class BorrarNivel(ABMMixin,DeleteView):
    model = NivEducativo
    template_name = 'niveducativos/niveducativo_confirm_delete.html'
    
    def get_success_url(self):
        return reverse('niveducativos:lista-niveles')
    
class CrearNivel(ABMMixin,CreateView):
    model = NivEducativo
    template_name = 'niveducativos/crearnivel.html'
    form_class = NivelForm

    def get_success_url(self):
        return reverse('niveducativos:lista-niveles')