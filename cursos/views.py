from django.shortcuts import render, get_object_or_404
from .models import Curso
from categorias.models import Categorias
from carts.models import CartItem
from carts.views import _get_card_id
def Cursos(request, category_slug=None):
    categories = None
    cursos = None
    curso_count = 0  # Inicializamos curso_count aquí

    if category_slug is not None:
        categories = get_object_or_404(Categorias, category_slug=category_slug)
        cursos = Curso.objects.filter(category=categories, is_available=True)
        curso_count = cursos.count()
    else:
        cursos = Curso.objects.all().filter(is_available=True)
        curso_count = cursos.count()

    context = {
        'cursos': cursos,
        'curso_count': curso_count,
    }

    return render(request, 'cursos/CursosEstudiante.html', context)

    #en esta creamos la consulta de pagina detalle de producto
def curso_detail(request, category_slug, curso_slug):
    try:    # get() args: el slug de mi categoria a la pertenece el producto se valide igualandolo con category_slug de la funcion
        single_curso = Curso.objects.get(category__category_slug=category_slug,slug=curso_slug)
        in_cart=CartItem.objects.filter(cart__cart_id = _get_card_id(request), curso = single_curso).exists()
    except Exception as e:
        raise e
    context={
        'single_curso':single_curso,
        'in_cart': in_cart
   }
    return render(request, 'cursos/product_detail.html',context)

