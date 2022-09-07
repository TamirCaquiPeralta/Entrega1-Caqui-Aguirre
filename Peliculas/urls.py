from django.urls import path
from Peliculas.views import peliculas, terror, accion, comedia, inicio



urlpatterns = [
    path('', peliculas),
    path('terror/', terror, name = 'Terror'),
    path('acción/', accion, name = 'Acción'),
    path('comedia/', comedia, name = 'Comedia'),
    path('inicio/', inicio, name = 'Inicio'),
]