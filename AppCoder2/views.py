from django.http import HttpResponse
from django.shortcuts import render
from AppCoder2.models import Curso
# Create your views here.

def curso(self):
    curso = Curso(nombre="Curso de Python", comision=212)
    curso.save()
    texto = f"Curso creado: {curso.nombre} {curso.comision}"
    return HttpResponse(texto)

def inicio(request):
    return render(request,'AppCoder2/inicio.html')

def cursos(request):
    return render(request,'AppCoder2/cursos.html')

def profesores(request):
    return render(request,'AppCoder2/profesores.html')  

def estudiantes(request):
    return render(request,'AppCoder2/estudiantes.html')

def entregables(request):
    return render(request,'AppCoder2/entregables.html')