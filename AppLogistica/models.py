from django.db import models
from django import forms

# Create your models here.
class proveedor(models.Model):
    cuit=models.CharField(max_length=20)
    razon_social=models.CharField(max_length=25)
    telefono=models.CharField(max_length=25)
    Correo=models.EmailField()

    def __str__(self):
        return f'Razón Social: {self.razon_social}--------CUIT: {self.cuit}'

class cliente(models.Model):
    cuit=models.CharField(max_length=20)
    razon_social=models.CharField(max_length=25)
    telefono=models.CharField(max_length=25)
    Correo=models.EmailField()

    def __str__(self):
        return f'Razón Social: {self.razon_social}--------CUIT: {self.cuit}'

class chofer(models.Model):
    nombre=models.CharField(max_length=25)
    dni=models.CharField(max_length=25)
    vto_licencia=models.DateField()
    vto_linti=models.DateField()

    def __str__(self):
        return f'Nombre: {self.nombre}--------DNI: {self.dni}'

class unidad(models.Model):
    patente=models.CharField(max_length=20)
    tipo=models.CharField(max_length=20)
    vto_vtv=models.DateField()
    vto_ruta=models.DateField()

    def __str__(self):
        return f'Patente: {self.patente}--------Tipo: {self.tipo}'

class carga(models.Model):
    fecha=models.DateField()
    origen=models.CharField(max_length=20)
    destino=models.CharField(max_length=20)
    tipo_carga=models.CharField(max_length=10)
    cantidad=models.IntegerField()

    def __str__(self):
        return f'fecha: {self.fecha}--------DNI: {self.origen}'

