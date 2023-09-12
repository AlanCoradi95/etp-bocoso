from django.db import models

# Create your models here.
class NivEducativo(models.Model):
    nombre= models.CharField(max_length=40, default='Sin especificar')

    class Meta:
        managed = True
        db_table = 'niveducativo'

    def __str__(self):
        return self.nombre