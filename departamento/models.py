from django.db import models

# Create your models here.

class Camisa(models.Model):
    time = models.CharField(max_length=30)
    jogador = models.CharField(max_length=30)
    numero = models.CharField(max_length=3)
    tamanho = models.CharField(max_length=1)

class Casual(models.Model):
    esporte = models.CharField(max_length=30)
    cor = models.CharField(max_length=30)
    tipo = models.CharField(max_length=10)
