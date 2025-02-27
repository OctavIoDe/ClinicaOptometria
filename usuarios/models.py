# Django
from django.db import models
from django.utils import timezone

# Modelos
from django.contrib.auth.models import AbstractUser, Group

ROL_OPCIONES = (
    ('M', 'Medico'),  
    ('S', 'Secretaria'),  
    ('G', 'Gerencia'), 
    ('V', 'Venta'),
    ('T', 'Taller') 
)

class Usuario(AbstractUser):
    rol = models.CharField(max_length=1, default='S', choices=ROL_OPCIONES, verbose_name="Sector")
    dni = models.CharField(max_length=11, verbose_name="Documento")
    nombre = models.CharField(max_length=25, verbose_name="Nombre")
    apellido = models.CharField(max_length=25, verbose_name="Apellido")
    ultima_actividad = models.DateTimeField(verbose_name="Última actividad", blank=True, null=True)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"


class Actividad(models.Model):
    
    #Cada interación con el sistema por parte de los empleados
    #registrará una nueva actividad. 
    
    accion = models.CharField(max_length=100, verbose_name="Acción")
    usuario = models.CharField(max_length=100, verbose_name="Usuario")
    momento = models.DateTimeField(verbose_name="Momento de la acción")

    def __str__(self):
        return self.acccion


def registrarActividad(request, mensaje):
    u_username = request.user.username
    u_nombre = f'{request.user.nombre} {request.user.apellido}'
    u_dni = request.user.dni
    usuario_actual = f'{u_username}, {u_nombre}, {u_dni}'
    accion_actual = mensaje
    Actividad.objects.create(accion=accion_actual, usuario=usuario_actual, momento=timezone.now())
    usuario_actual = Usuario.objects.get(id=request.user.id)
    usuario_actual.ultima_actividad = timezone.now()
    usuario_actual.save()