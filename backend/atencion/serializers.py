from rest_framework import serializers
from .models import Usuario, PuntoAtencion, Turno

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'email', 'cedula', 'password']
        extra_kwargs = {'password': {'write_only': True}}  # No devolver la contraseña

    def create(self, validated_data):
        user = Usuario.objects.create_user(
            email=validated_data['email'],
            cedula=validated_data['cedula'],
            password=validated_data['password']
        )
        return user

class PuntoAtencionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PuntoAtencion
        fields = ['id', 'nombre', 'descripcion']

class TurnoSerializer(serializers.ModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all())
    punto_atencion = serializers.PrimaryKeyRelatedField(queryset=PuntoAtencion.objects.all())

    class Meta:
        model = Turno
        fields = ['id', 'usuario', 'punto_atencion', 'numero_ticket', 'prioridad', 'fecha_creacion', 'atendido']

    def validate_numero_ticket(self, value):
        if not value.startswith(('P-', 'N-')) or not value[2:].isdigit():
            raise serializers.ValidationError("El número de ticket debe ser 'P-xxx' o 'N-xxx' con dígitos.")
        return value