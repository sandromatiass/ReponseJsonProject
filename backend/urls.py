from django.urls import path
from usuarios.views import home_page, UsuarioJSONAPI

urlpatterns = [
    path('', home_page, name='home'),
    path('api/usuarios/', UsuarioJSONAPI.as_view(), name='api-usuarios'),  
]