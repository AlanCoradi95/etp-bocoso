from django.urls import path
from . import views

app_name = 'comentarios'

urlpatterns = [
    path('comentario/',views.CrearComentario, name="comentario"),
]