from django.shortcuts import render
from .models import Curso

def Cursos(request):
    #Traer todos los cursos que esten activos
    cursos = Curso.objects.all().filter(is_available=True)
    curso_count=cursos.count()
    #Envolvemos el resultado dentro de un diccionario
    context={
        'cursos':cursos, 
        'curso_count':curso_count,
    }
                                #indicamos que el context se envie a la pagina
    return render(request,'cursos/CursosEstudiante.html',context)