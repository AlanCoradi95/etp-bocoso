from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('registro/',views.UsuarioCreateView.as_view(template_name="usuarios/registro.html"), name = 'registro'),
    path('login/',auth_views.LoginView.as_view(template_name="usuarios/login.html"), name='login'),
    path('logout/',auth_views.logout_then_login,name='logout'),
    path('lista-usuarios/',views.listaUsuarios, name="lista-usuarios"),
    path('editar-perfil/<int:pk>',views.editarPerfil,name= "editar-perfil"),
    
]