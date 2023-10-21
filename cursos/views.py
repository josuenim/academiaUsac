from django.shortcuts import render, get_object_or_404
from .models import Curso
from categorias.models import Categorias

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
