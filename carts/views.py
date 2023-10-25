from django.shortcuts import render,redirect,get_object_or_404
from cursos.models import Curso
from .models import  Cart,CartItem
from django.core.exceptions import ObjectDoesNotExist
#Funcion para realizar la busqueda de la sesion del usuario actual dentro del browser
# _cart.. guion bajo indicanod que es una funcion privada


#Funcion que me permite buscar en mi carrito de compras
#Utilizando como parametro el objeto request.   
def _get_card_id(request):
    cart= request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart


def add_cart(request, curso_id):
    #condicion que busque por el id
    curso = Curso.objects.get(id=curso_id)
    try:
        cart = Cart.objects.get(cart_id=_get_card_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_get_card_id(request))
    cart.save()

    try:
        cart_item= CartItem.objects.get(curso=curso,cart=cart)
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item=CartItem.objects.create(
            curso = curso,
            quantity =1,
            cart=cart,
        )
        #Guardamos el recort en la base de datos
        cart_item.save()
    return redirect('cart')


def remove_cart_item(request,curso_id):
    cart = Cart.objects.get(cart_id=_get_card_id(request))
    curso =get_object_or_404(Curso,id=curso_id)
    cart_item=CartItem.objects.get(curso=curso,cart=cart)
    cart_item.delete()
    return redirect('cart')     


def cart(request,total=0,quantity=0,cart_items=None):
    try:
        cart=Cart.objects.get(cart_id=_get_card_id(request))
        cart_items=CartItem.objects.filter(cart=cart,is_active=True)
        valor=1
        #Saber el precio total de mis cursos
        for cart_item in cart_items:
                    # llamamos al campo 'curso' de mi clase CartItem
            total += cart_item.curso.costo
            #cantidad total de cursos
            quantity += cart_item.quantity   
    # si no encontramos los valores
    except ObjectDoesNotExist:
        valor=0
        print("error")
        pass #ignora la axception
    #dic indicar que  valores son los que se tiene que enviar al template cart  
    context = {
        'total':total,
        'quantity':quantity,
        'cart_items':cart_items,
        'prueba': valor,
    }
    return render(request, 'cursos/asignacion_curso.html', context)

