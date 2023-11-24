from django.db import models
from cursos.models import Curso
# Create your models here.

#Estructura del carrito de compra. Padre de Cart_item
class Cart(models.Model):
    cart_id= models.CharField(max_length=250, blank=True)
    date_added= models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id
 
#Cart_Id o producto selecciona que sera seleccionado y comprado
class CartItem(models.Model):
    curso=models.ForeignKey(Curso,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    is_active=models.BooleanField(default=True)
    nota = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)


    def sub_total(self):
        return self.curso.costo * self.quantity
    #funcion _str_ devuelve un objeto de tipo strig pero el tipo
    #de objeto que necesitamos es de tipo curso
    def __unicode__(self):
        return self.curso

