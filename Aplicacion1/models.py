from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    edad=models.IntegerField()
    correo=models.EmailField(max_length=50)


class Contacto(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    correo=models.EmailField(max_length=50)
    mensaje=models.TextField(max_length=200)
    
    
   
    