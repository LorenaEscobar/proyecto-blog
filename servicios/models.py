from pickle import TRUE
from tabnanny import verbose
from django.db import models

# Create your models here.
class Servicio(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='servicios') #crea automáticamente y guarda las imágenes
    created=models.DateTimeField(auto_now_add=TRUE)
    updated=models.DateTimeField(auto_now_add=TRUE)

    class Meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'

    def __str__(self):
        return self.titulo