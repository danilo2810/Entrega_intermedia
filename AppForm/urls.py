from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio,name='inicio'),
    path('personas/', personas,name='personas'),
    path('productos/', productos,name='productos'),
    path('proveedores/', proveedores,name='proveedores'),
    path('busquedas/', busquedas,name='busquedas'),
    path('buscarUsuario/',buscarUsuario, name='buscarUsuario'),
    path('buscarProducto/',buscarProducto, name='buscarProducto'),
    path('buscarProveedor/',buscarProveedor, name='buscarProveedor'),
    path('buscarGeneral/',buscarGeneral, name='buscarGeneral'),
    
]