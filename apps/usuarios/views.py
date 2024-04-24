from django.shortcuts import render
from apps.usuarios.models import Estudiante
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from apps.usuarios.models import Curso
from django.shortcuts import  redirect
from .models import Estudiante
from django.views.generic import  ListView

class principal(ListView):
    """
    funcion de la vista principal
    """
    model=Estudiante
    template_name='registro.html'
    context_object_name='est'
    queryset=Estudiante.objects.all()
    
def registrar(request):
    """
    funcion que registra compus
    """
    if request.method== 'POST':
        nombre = request.POST['knombre']
        apellido = request.POST['kapellido']
        correo= request.POST['kcorreo']
        edad = request.POST['kedad']
        cursos = request.POST['kcursos']
        comp=Estudiante.objects.create(nombre=nombre,apellido=apellido,
                                correo=correo,edad=edad,cursos=cursos)
        return redirect('/')
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