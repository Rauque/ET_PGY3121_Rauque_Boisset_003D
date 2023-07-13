from django.urls import path
from mascotitas.views import *
urlpatterns = [
    path('', Inicio, name="Inicio"),
    path('accesperro/', accesperro , name="Acceosrios Perros"),
    path('accesgato/', accesgato , name="Accesorios Gatos"),
    path('mision/', mision , name="Mision"),
    path('registrar/', registrar , name="registrar"),
    path('vet/', vet , name="Veterinarios"),
    path('adoptar/', adoptar , name="Adoptar"),
    path('crear/', crear , name="Crear"),
    path('dos/', dos , name="dos"),
    path('eliminar/<id>', eliminar, name="eliminar"),
    path('modificar/<id>', modificar, name="modificar"),
    path('crear/', crear, name="crear"),
    path('tienda/',tienda, name="tienda"),
    path('tienda/',tienda, name="tienda"),
    path('tienda/<str:especie>/', tienda, name='tienda_especie'),
    path('generarBoleta/', generarBoleta,name="generarBoleta"),
    path('agregar/<id>', agregar_producto, name="agregar"),
    path('eliminar/<id>', eliminar_producto, name="eliminar"),
    path('restar/<id>', restar_producto, name="restar"),
    path('limpiar/', limpiar_carrito, name="limpiar"),
    path('carrito/', carrito, name="carrito"),
    path('descontar_stock/', descontar_stock, name="descontar_stock"),
    
]
