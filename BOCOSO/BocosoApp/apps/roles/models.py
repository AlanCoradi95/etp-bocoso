from django.db import models

# Create your models here.
class Rol(models.Model):
    nombre= models.CharField(max_length=40, default= 'Sin especificar')

    def __str__(self):
        return self.nombre
    
    class Meta:
        managed = True
        db_table = 'rol'