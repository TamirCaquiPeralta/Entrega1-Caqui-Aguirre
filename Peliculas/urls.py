from django.urls import path
from Peliculas.views import peliculas

urlpatterns = [
    path('', peliculas),
    
]