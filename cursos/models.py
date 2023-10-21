from django.db import models
from profesores.models import Profesor
from categorias.models import Categorias
# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    slug =models.CharField(max_length=100,blank=True)

    costo=models.PositiveIntegerField()
    horario=models.CharField(max_length=20) 
    cupo=models.PositiveIntegerField()
    cat_image=models.ImageField(upload_to= 'photos/cursos')
    descripcion = models.TextField(blank=True)
    is_available= models.BooleanField(default=True)
    creat_date=models.DateTimeField(auto_now_add=True)
    #category = models.CharField(max_length=200,blank=True)
    ##ForeignKey#
    profesor = models.ForeignKey(Profesor, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Categorias,on_delete=models.SET_NULL,null=True)
    ##
    #modified_date=models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name='Curso'
        verbose_name_plural = 'Cursos'
    #La data va a ser visible dentro del modulo de administracion de django
    #la data con valor representativo
    def __str__(self):
        return self.nombre
