from django.shortcuts import render

from django.http import HttpResponse

def peliculas(request):
    return render(request,'Peliculas/inicio.html')

def Terror(request):
    return render(request, 'Terror')
