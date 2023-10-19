from django.db import models
from django.db.models import CheckConstraint, Q

class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    dpi=models.IntegerField(help_text="Enter a positive integer.",unique=True)
    especialidad = models.CharField(max_length=50, blank=True)
    category = models.CharField(max_length=200,blank=True)

    class Meta:
        verbose_name='Profesor'
        verbose_name_plural = 'Profesores'
    def __str__(self):
        return "{} {} {}".format(self.nombre, self.apellido, self.especialidad)

