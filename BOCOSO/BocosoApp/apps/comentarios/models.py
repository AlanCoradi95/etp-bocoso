from django.db import models
from apps.usuarios.models import Usuario
from apps.noticias.models import Noticia
# Create your models here.
class Comentario(models.Model):
    titulo= models.CharField(max_length=255, null = True)
    descripcion= models.TextField(default=" - ")
    fecha= models.DateTimeField(auto_now_add=True)
    usuario= models.ForeignKey(Usuario, on_delete=models.SET_NULL, null = True)
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE,null = True)
    class Meta:
        managed = True
        db_table = 'comentario'