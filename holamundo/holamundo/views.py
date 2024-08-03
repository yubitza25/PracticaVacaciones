from django.http import HttpResponse
from .import views

def saludo(request):
    return HttpResponse("Hola mundo")

def despedida(request):
    return HttpResponse("Adios, no me hables")

def adulto(request, edad):
    if edad>= 18:
        return HttpResponse("Eres mayor de edad")
    else:
        return HttpResponse("Eres menor de edad")