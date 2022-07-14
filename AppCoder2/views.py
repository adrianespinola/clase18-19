from django.http import HttpResponse
from django.shortcuts import render
from AppCoder2.models import Curso
# Create your views here.

def curso(sefl):
    curso = Curso(nombre="Curso de Python", comision=212)
    curso.save()
    texto = f"Curso creado: {curso.nombre} {curso.comision}"
    return HttpResponse(texto)