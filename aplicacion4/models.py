from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# Create your models here.


class Servicio(models.Model):
    nombre = models.CharField(max_length=40)
    tiempo = models.CharField(max_length=40)


class Consola(models.Model):
    nombre = models.CharField(max_length=40)
    año = models.CharField(max_length=40)
    estado = models.CharField(max_length=40)
    stock = models.IntegerField()


class Juego(models.Model):
    nombre = models.CharField(max_length=60)
    consola = models.CharField(max_length=60)
    stock = models.IntegerField()


class Cliente(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    email = models.EmailField()
