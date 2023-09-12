from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.roles.models import Rol
# Create your models here.
class Usuario(AbstractUser):
    foto = models.ImageField(upload_to='usuarios', null=True, blank=True,default='usuarios/usuario-default.png')
    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null= True)

    class Meta:
        managed= True
        db_table = 'usuario'
