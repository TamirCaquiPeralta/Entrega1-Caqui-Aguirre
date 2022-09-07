from django.db import models

class Terror(models.Model):
    Titulo = models.CharField (max_length= 99)

class Acción(models.Model):
    Titulo = models.CharField (max_length= 99)

class Comedia(models.Model):
    Titulo = models.CharField(max_length= 99) 
