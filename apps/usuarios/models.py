from django.db import models



class Curso(models.Model):
    nombre = models.CharField( max_length=50)
    
    

class Estudiente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(unique=True)
    fecha_nacimiento = models.DateField()
    edad = models.models.IntegerField()
    estado = models.BooleanField(default=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    

class Materia(models.Model):
    nombre = models.CharField(max_length=50)