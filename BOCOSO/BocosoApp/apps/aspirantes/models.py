from django.db import models

# Create your models here.
class Aspirante(models.Model):
    nombre = models.CharField(max_length=40, default='Sin Especificar')
    apellido=models.CharField(max_length=40,default='Sin Especificar')
    telefono= models.BigIntegerField(default='0')
    email= models.EmailField(default='Sin Especificar')
    comentario = models.TextField(blank=True)
    cv = models.FileField(upload_to='aspirantes',blank=True)
    class Meta:
        managed = True
        db_table = 'aspirante'