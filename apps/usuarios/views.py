from django.shortcuts import render
from apps.usuarios.models import Estudiante
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from apps.usuarios.models import Curso


#CREAR CURSO

def crear_curso(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        
        curso =  Curso.objects.create(
            nombre = nombre
        )
        return redirect('listar_curso')
    else:
        return render(request, 'curso/crear_curso.html')


def listar_curso(request):
    curso = Curso.objects.all() 
    return render(request,'curso/listar_curso.html', {'curso':curso})