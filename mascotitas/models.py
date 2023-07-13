import datetime
from distutils.command.upload import upload
from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class Especie(models.Model):
    idEspecie = models.IntegerField(primary_key=True, verbose_name="Id de Especie")
    nombreEspecie=models.CharField(max_length=50, blank=True, verbose_name="Nombre de Especie")

    def __str__(self):
        return self.nombreEspecie

class Tamaño(models.Model):
    idTamaño = models.IntegerField(primary_key=True, verbose_name="Id de Tanaño")
    nombreTamaño=models.CharField(max_length=50, blank=True, verbose_name="Nombre de Tamaño")
    
    def __str__(self):
        return self.nombreTamaño


class Animal(models.Model):
    nombre=models.CharField(primary_key=True, max_length=15, verbose_name="Nombre")
    genero=models.CharField(max_length=50, blank=True, verbose_name="Genero")
    imagen=models.ImageField(upload_to="imagenes", null=True, blank=True, verbose_name="Imagen")
    especie=models.ForeignKey(Especie, on_delete=models.CASCADE, verbose_name="Especie")
    tamaño=models.ForeignKey(Tamaño, on_delete=models.CASCADE, verbose_name="Tamaño")
    descripcion=models.CharField(max_length=150, blank=True, verbose_name="Descripcion")


    def __str__(self):
        return self.nombre


class Mercancia(models.Model):
    nombre=models.CharField(primary_key=True, max_length=15, verbose_name="Nombre")
    imagen=models.ImageField(upload_to="imagenes", null=True, blank=True, verbose_name="Imagen")
    especie=models.ForeignKey(Especie, on_delete=models.CASCADE, verbose_name="Especie")
    descripcion=models.CharField(max_length=150, blank=True, verbose_name="Descripcion")
    precio = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre
    

class Boleta(models.Model):
    id_boleta = models.AutoField(primary_key=True)
    envio = models.BigIntegerField(default=2000)  
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    total_imp = models.BigIntegerField(default=0)  
    total = models.BigIntegerField(default=0)  
    fechaCompra = models.DateTimeField(blank=False, null=False, default=datetime.datetime.now)
    
    def __str__(self):
        return str(self.id_boleta)

class detalle_boleta(models.Model):
    id_boleta = models.ForeignKey('Boleta', blank=True, on_delete=models.CASCADE)
    id_detalle_boleta = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey('Mercancia', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.BigIntegerField()
    subtotal_imp = models.BigIntegerField(default=0)  

    def __str__(self):
        return str(self.id_detalle_boleta)
