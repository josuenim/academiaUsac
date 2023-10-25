from django.db import models
from categorias.models import Categorias


class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    dpi=models.IntegerField(help_text="Enter a positive integer.",unique=True)
    especialidad = models.CharField(max_length=50, blank=True)
    category = models.ForeignKey(Categorias,on_delete=models.SET_NULL,null=True)

    class Meta:
        verbose_name='Profesor'
        verbose_name_plural = 'Profesores'
    def __str__(self):
        return "{} {} {}".format(self.nombre, self.apellido, self.especialidad)

