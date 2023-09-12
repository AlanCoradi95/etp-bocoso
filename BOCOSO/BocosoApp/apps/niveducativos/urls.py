from django.urls import path
from . import views

app_name = 'niveducativos'

urlpatterns = [
    path('lista-niveles/',views.listaNiveducativos,name="lista-niveles"),
    path('eliminar-nivel/<int:pk>',views.BorrarNivel.as_view(), name='borrar-nivel'),
    path('crear-nivel',views.CrearNivel.as_view(),name="crear-nivel")
]