from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Usuario, PuntoAtencion, Turno
from .serializers import UsuarioSerializer, PuntoAtencionSerializer, TurnoSerializer

# Usuarios
class UsuarioCreateView(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioListView(generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAdminUser]  # Solo admins ven la lista

# Puntos de Atención
class PuntoAtencionListCreateView(generics.ListCreateAPIView):
    queryset = PuntoAtencion.objects.all()
    serializer_class = PuntoAtencionSerializer
    permission_classes = [IsAuthenticated]  # Autenticados pueden crear/listar

class PuntoAtencionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PuntoAtencion.objects.all()
    serializer_class = PuntoAtencionSerializer
    permission_classes = [IsAdminUser]  # Solo admins editan/eliminan

# Turnos
class TurnoListCreateView(generics.ListCreateAPIView):
    queryset = Turno.objects.all()
    serializer_class = TurnoSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Generar número de ticket automáticamente
        prioridad = serializer.validated_data['prioridad']
        ultimo_turno = Turno.objects.filter(prioridad=prioridad).order_by('-numero_ticket').first()
        if ultimo_turno:
            numero = int(ultimo_turno.numero_ticket[2:]) + 1
        else:
            numero = 1
        serializer.save(numero_ticket=f"{prioridad}-{str(numero).zfill(3)}")

class TurnoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Turno.objects.all()
    serializer_class = TurnoSerializer
    permission_classes = [IsAuthenticated]