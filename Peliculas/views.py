from django.shortcuts import render

from django.http import HttpResponse

from Peliculas.models import Terror, Acción, Comedia 

def peliculas(request):
    return render(request,'Peliculas/inicio.html')

def terror(request):
    return render(request,'Peliculas/terror.html')


def accion(request):
    return render(request,'Peliculas/acción.html')

def comedia(request):
    return render(request,'Peliculas/comedia.html')

def inicio(request):
    return render(request, 'Peliculas/inicio.html')