from django.db import models

class Director(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    anio_estreno = models.IntegerField()
    genero = models.CharField(max_length=50)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo