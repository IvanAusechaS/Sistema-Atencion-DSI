from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class PuntoAtencion(models.Model):
    nombre = models.CharField(max_length=100, unique=True)  # Ej. "Melendez", "Polvorines"
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Turno(models.Model):
    PRIORIDAD_CHOICES = (
        ('P', 'Prioridad Alta'),
        ('N', 'Normal'),
    )
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    punto_atencion = models.ForeignKey(PuntoAtencion, on_delete=models.CASCADE)
    numero_ticket = models.CharField(max_length=10, unique=True)  # Ej. "P-001", "N-101"
    prioridad = models.CharField(max_length=1, choices=PRIORIDAD_CHOICES)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    atendido = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.numero_ticket} - {self.punto_atencion}"