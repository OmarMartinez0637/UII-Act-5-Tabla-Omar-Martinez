from django.db import models

# Create your models here.
# clase Menu con los campos nombre, precio y descripcion
class Menu(models.Model):
    nombre= models.CharField(max_length=100)
    precio= models.FloatField()
    descripcion= models.CharField(max_length=200)