from django.shortcuts import render

def index(request):
    template_name = 'index.html'

    return render(request,template_name)

def quienessomos(request):
    template_name = 'quienessomos.html'

    return render(request,template_name)

def noticias(request):
    template_name = 'noticias/listanoticias.html'

    return render(request,template_name)

def bienestar(request):
    template_name = 'bienestar.html'

    return render(request,template_name)

def niveducativo(request):
    template_name = 'niveducativos.html'

    return render(request, template_name)