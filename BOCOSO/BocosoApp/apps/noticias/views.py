from django.contrib import messages
from django.shortcuts import render,redirect
from .forms import CrearNoticiaForm
from .models import Noticia
from utils.mixins import ABM, ABMMixin
from apps.comentarios.models import Comentario
from apps.comentarios.forms import CrearComentarioForm
from django.views.generic.edit import DeleteView
from django.urls import reverse
# Create your views here.

@ABM()
def CrearNoticia(request):
    template_name = 'noticias/crearnoticia.html'
    form = CrearNoticiaForm()
    
    if request.method == 'POST':
        form = CrearNoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            noticia = form.save(commit=False)
            noticia.usuario_id = request.user.id
            noticia.tipo = 1
            noticia.save()
            messages.success(request, f"Noticia creada correctamente")
            return redirect('noticias:lista-noticias')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
    
    contexto = {
        'form' : form
    }
    return render(request,template_name,contexto)

@ABM()
def CrearNoticiaBE(request):
    template_name = 'noticias/crearnoticiabe.html'
    form = CrearNoticiaForm()
    
    if request.method == 'POST':
        form = CrearNoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            noticia = form.save(commit=False)
            noticia.usuario_id = request.user.id
            noticia.tipo = 2
            noticia.save()
            messages.success(request, f"Noticia creada correctamente")
            return redirect('noticias:lista-noticias-be')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
    
    contexto = {
        'form' : form
    }
    return render(request,template_name,contexto)


def listaNoticias(request):
    template_name = 'noticias/listanoticias.html'
    noticias = Noticia.objects.filter(tipo = 1).order_by('-fecha')
    contexto = {
        'noticias':noticias
    }

    return render(request,template_name,contexto)

def listaNoticiasBE(request):
    template_name = 'noticias/listanoticiasbe.html'
    noticias = Noticia.objects.filter(tipo = 2).order_by('-fecha')
    contexto = {
        'noticias':noticias
    }

    return render(request,template_name,contexto)

def verNoticia(request,pk):
    template_name = 'noticias/noticia.html'
    noticia = Noticia.objects.get(pk=pk)
    comentarios = Comentario.objects.filter(noticia = pk).order_by('-fecha')
    form = CrearComentarioForm

    if request.method == 'POST':
        form = CrearComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario_id = request.user.id
            comentario.noticia_id = pk
            comentario.save()
            messages.success(request, f"Noticia creada correctamente")
            return redirect('noticias:noticia',pk=pk)
       


    contexto = {
        'noticia': noticia,
        'comentarios': comentarios,
        'form': form,
    }

    return render(request,template_name,contexto)

@ABM()
def editarNoticia(request, pk):
    template_name = 'noticias/crearnoticia.html'
    noticia = Noticia.objects.get(pk=pk)
    form = CrearNoticiaForm(instance=noticia)

    if request.method == 'POST':
        form = CrearNoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            noticia.titulo = request.POST['titulo']
            noticia.descripcion = request.POST['descripcion']
            noticia.save()

        return redirect('noticias:noticia',pk)
    
    contexto = {
        'form': form
    }

    return render(request, template_name, contexto)

class BorrarNoticia(ABMMixin,DeleteView):
    model = Noticia
    template_name = 'noticias/noticia_confirm_delete.html'
    def get_success_url(self):
        return reverse('noticias:lista-noticias')
