from django.db import models
from apps.niveducativos.models import NivEducativo
# Create your models here.
class Inscripcion(models.Model):
    nombre = models.CharField(max_length=40, default='Sin Especificar')
    apellido = models.CharField(max_length=40, default='Sin Especificar')
    dni = models.BigIntegerField()
    telefono = models.BigIntegerField(null=True)
    direccion = models.CharField(max_length=255,default='Sin Especificar')
    email = models.EmailField(default='Sin especificar')
    niveducativo = models.ForeignKey(NivEducativo, on_delete=models.SET_NULL, null=True)

    class Meta:
        managed: True
        db_table = 'inscripcion'