from django.db import models

# Create your models here.

class familiar1(models.Model):

    nombre = models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    edad = models.IntegerField()
    nacimiento = models.DateField()
    experiencia = models.CharField(max_length = 40)

class familiar2(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    nacimiento = models.DateField()
    experiencia = models.CharField(max_length=40)

class familiar3(models.Model):

    nombre = models.CharField(max_length=40)    
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    nacimiento = models.DateField()
    experiencia = models.CharField(max_length=40)