from django.shortcuts import render,redirect
from .models import Inscripcion
from django.views.generic.edit import CreateView
from django.urls import reverse
from .forms import CrearInscripcionForm
from apps.niveducativos.models import NivEducativo

# Create your views here.
class CrearInscripcion(CreateView):
    model = Inscripcion
    template_name = 'inscripciones/inscripcion.html'
    form_class = CrearInscripcionForm
    
    def get_success_url(self):
        return reverse('index')
    
def crearIncripcion(request):
    template_name = 'inscripciones/inscripcion.html'
    niveducativos = NivEducativo.objects.all()
    form = CrearInscripcionForm()

    if request.method == 'POST':
        form = CrearInscripcionForm(request.POST)
        if form.is_valid():
            noticia = form.save(commit=False)
            noticia.save()
            return redirect('index')
        

    contexto = {
        'niveducativos' : niveducativos,
        'form': form
    }
    return render(request,template_name,contexto)

def listaInscripciones(request):
    template_name = 'inscripciones/listainscripciones.html'
    inscripciones = Inscripcion.objects.all()
    contexto = {
        'inscripciones': inscripciones
    }
    return render(request,template_name,contexto)
