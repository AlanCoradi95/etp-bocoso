from django.urls import path
from . import views

app_name = 'aspirantes'

urlpatterns = [
    path('aplicar/', views.CrearAspirantes.as_view(), name='aplicar'),
    path('lista-aplicantes/',views.listaAplicantes, name="lista-aplicantes"),
]