from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

class CustomUserManager(UserManager):
    def create_superuser(self, email, password, cedula, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, cedula, **extra_fields)

    def create_user(self, email, password, cedula, **extra_fields):
        if not email:
            raise ValueError('El correo electrónico es obligatorio.')
        if not cedula:
            raise ValueError('La cédula es obligatoria.')
        email = self.normalize_email(email)
        user = self.model(email=email, cedula=cedula, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

class Usuario(AbstractUser):
    email = models.EmailField(unique=True)
    cedula = models.CharField(max_length=20, unique=True)
    username = models.CharField(max_length=150, blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['cedula']

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.email} ({self.cedula})"

class PuntoAtencion(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
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
    numero_ticket = models.CharField(max_length=10, unique=True)
    prioridad = models.CharField(max_length=1, choices=PRIORIDAD_CHOICES)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    atendido = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.numero_ticket} - {self.punto_atencion}"