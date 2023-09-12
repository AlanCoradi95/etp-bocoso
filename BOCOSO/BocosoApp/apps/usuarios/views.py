from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView,UpdateView
from .models import Usuario
from django.urls import reverse
from .forms import UsuarioForm,EditaRol,EditarUsuarioForm
from utils.mixins import ABM,es_el_usuario
from apps.roles.models import Rol

# Create your views here.

class UsuarioCreateView(CreateView):
    model = Usuario
    template_name = 'usuarios/registro.html'
    form_class = UsuarioForm

    def get_success_url(self):
        return reverse('usuarios:login')

@ABM()
def listaUsuarios(request):
    template_name = 'usuarios/listausuarios.html'
    usuarios = Usuario.objects.all()
    roles = Rol.objects.all()
    form = EditaRol()
    if request.POST:
        rol = Rol.objects.get(pk = request.POST.get('rol'))
        usuario = Usuario.objects.get(pk = request.POST.get('pk'))
        form = EditaRol(request.POST,instance=usuario)
        if form.is_valid():
            form.save()
            
        return redirect('usuarios:lista-usuarios')
    
    contexto = {
        'usuarios': usuarios,
        'roles': roles
    }

    return render(request,template_name, contexto)

@es_el_usuario()
def editarPerfil(request,pk):
    template_name = 'usuarios/perfil.html'
    usuario = Usuario.objects.get(pk=pk)
    form = EditarUsuarioForm(instance = usuario)
    if request.method == 'POST':
        form = EditarUsuarioForm(request.POST,request.FILES)
        if form.is_valid():
            usuario.first_name = request.POST.get('first_name')
            usuario.last_name = request.POST.get('last_name')
            usuario.foto = request.FILES.get('foto')
            usuario.email = request.POST.get('email')
            usuario.save()
            return redirect('usuarios:editar-perfil',pk)
        
    contexto = {
        'form': form,
        
    }
    return render(request,template_name,contexto)

class EditarUsuario(UpdateView):
    model = Usuario
    template_name = 'usuarios/perfil.html'
    form_class = UsuarioForm

    def get_success_url(self):
        return reverse('index')
