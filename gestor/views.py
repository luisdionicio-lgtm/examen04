from django.shortcuts import render
from .models import Pelicula, Director

def lista_peliculas(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'gestor/peliculas.html', {'peliculas': peliculas})


def lista_directores(request):
    directores = Director.objects.all()
    return render(request, 'gestor/directores.html', {'directores': directores})