from django.db import models
from apps.usuarios.models import Usuario
# Create your models here.
class Noticia(models.Model):
    titulo = models.CharField(max_length= 255,default='Sin Especificar')
    descripcion = models.TextField()
    usuario = models.ForeignKey(Usuario,on_delete=models.SET_NULL, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    portada = models.ImageField(upload_to='noticias',null=True,blank=True,default='noticias/portada-default.jpg')
    tipo = models.IntegerField(default=1)
    class Meta:
        managed = True
        db_table = 'noticia'