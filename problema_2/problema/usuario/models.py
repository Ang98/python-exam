from django.db import models

# Create your models here.
class Usuario(models.Model):

    nombres = models.CharField(max_length=45, blank=True, default='')
    apellido_p = models.CharField(max_length=45, blank=True, default='')
    apellido_m = models.CharField(max_length=45, blank=True, default='')
    edad = models.IntegerField()

    def __str__(self):
        
        return self.nombres + " " + self.apellido_p + "" + self.apellido_m