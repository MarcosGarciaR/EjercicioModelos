from django.db import models
from django.utils import timezone

# Create your models here.
class Usuario(models.Model):    
    nombre = models.CharField(max_length=100)
    correoElectronico = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    fechaRegistro = models.DateTimeField(default=timezone.now)


class Tarea(models.Model):
    OPCIONES_ESTADO = [
        ('pend', 'Pendiente'),
        ('prog', 'Progreso'),
        ('comp', 'Completada')
    ]
    
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    prioridad = models.IntegerField()
    estado = models.CharField(max_length=20, choices=OPCIONES_ESTADO)
    completada = models.BooleanField(default=False)
    fechaCreacion = models.DateField()
    horaVencimiento = models.TimeField()


class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracionEstimada = models.FloatField()
    fechaInicio = models.DateField()
    fechaFinalizacion = models.DateField()
    
    proyectosAsignados = models.ManyToManyField(Usuario, related_name="Usuario_Colaborador")



class Etiqueta(models.Model):
    nombre = models.CharField(max_length=100, unique=True)


class AsignacionDeTarea(models.Model):
    observaciones = models.TextField()
    fechaAsignacion = models.DateTimeField()


class Comentario(models.Model):
    contenido = models.TextField()
    fechaComentario = models.DateTimeField()

