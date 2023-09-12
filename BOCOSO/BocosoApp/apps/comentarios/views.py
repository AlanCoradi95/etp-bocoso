from django.shortcuts import render,redirect
from .forms import CrearComentarioForm

# Create your views here.
def CrearComentario(request):
    template_name = 'comentarios/comentario.html'
    form = CrearComentarioForm()
    
    if request.method == 'POST':
        form = CrearComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario_id = request.user.id
            comentario.save()

        return redirect('index')
    
    contexto = {
        'form' : form
    }
    return render(request,template_name,contexto)