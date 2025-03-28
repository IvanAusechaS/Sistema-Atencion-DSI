from django.urls import path
from .views import (
    UsuarioCreateView, UsuarioListView,
    PuntoAtencionListCreateView, PuntoAtencionDetailView,
    TurnoListCreateView, TurnoDetailView
)

urlpatterns = [
    path('usuarios/', UsuarioListView.as_view(), name='usuario-list'),
    path('usuarios/crear/', UsuarioCreateView.as_view(), name='usuario-create'),
    path('puntos-atencion/', PuntoAtencionListCreateView.as_view(), name='punto-atencion-list-create'),
    path('puntos-atencion/<int:pk>/', PuntoAtencionDetailView.as_view(), name='punto-atencion-detail'),
    path('turnos/', TurnoListCreateView.as_view(), name='turno-list-create'),
    path('turnos/<int:pk>/', TurnoDetailView.as_view(), name='turno-detail'),
]