from django.urls import path
from . import views

app_name = 'noticias'

urlpatterns = [
    path('crear-noticia/', views.CrearNoticia, name = "crear-noticia"),
    path('lista-noticias/',views.listaNoticias, name = "lista-noticias"),
    path('noticia/<int:pk>',views.verNoticia,name = 'noticia'),
    path('editar-noticia/<int:pk>',views.editarNoticia,name='editar-noticia'),
    path('eliminar-noticia/<int:pk>',views.BorrarNoticia.as_view(), name='borrar-noticia'),
    path('lista-bienestar/', views.listaNoticiasBE,name="lista-noticias-be"),
    path('crear-noticia-be/',views.CrearNoticiaBE, name="crear-noticia-be")
]