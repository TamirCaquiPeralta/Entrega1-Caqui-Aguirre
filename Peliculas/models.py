from django.db import models

class Terror(models.Model):
    Titulo = models.CharField (max_length= 99)
pass
class Acción(models.Model):
    Titulo = models.CharField (max_length= 99)
pass
class Comedia(models.Model):
    Titulo = models.CharField(max_length= 99) 
pass