from django.urls import path
from .views import UsuarioListAPIView

urlpatterns = [
    path('usuarios/', UsuarioListAPIView.as_view(), name='usuarios-list'),
]