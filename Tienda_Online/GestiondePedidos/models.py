from django.db import models

# Create your models here.

class Clientes(models.Model):
    Nombre = models.CharField(max_length=40)
    Direccion = models.CharField(max_length=50)
    Email = models.EmailField()
    Telefono = models.CharField(max_length=10)

class Articulos(models.Model):
    Nombre = models.CharField(max_length=20)
    Seccion = models.CharField(max_length=30)
    Precio = models.IntegerField()

class Pedidos(models.Model):
    Numero = models.IntegerField()
    Fecha = models.DateField()
    Entregado = models.BooleanField()