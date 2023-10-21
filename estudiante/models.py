from django.db import models


class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    #dpi=models.IntegerField(help_text="Enter a positive integer.",unique=True)
    

    class Meta:
        verbose_name='Estudiante'
        verbose_name_plural = 'Estudiantes'
    def __str__(self):
        return "{} {} ".format(self.nombre, self.apellido)
