from django.urls import path
from . import views

app_name = 'inscripciones'

urlpatterns = [
    path('inscripcion/', views.crearIncripcion, name='inscripcion'),
    path('inscripciones/',views.listaInscripciones, name='lista-inscripciones')
]