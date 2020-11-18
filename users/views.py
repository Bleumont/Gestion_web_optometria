from django.shortcuts import render
from django.http import HttpResponse
from .models import Pacientes, Pedidos, Productos, Profesionales, Turnos

# Create your views here.
def index(request):
    return render(request, 'users/index.html')

def login(request):
    return render(request, 'users/login.html')

def management(request):
    return render(request, 'users/management.html')

def medicos(request):
    return HttpResponse("Hola medico!")

def taller(request):
    return HttpResponse("Hola medico!")

def secretaria(request):
    return HttpResponse("Hola secretaria!")

def gerencia(request):
    return HttpResponse("Hola gerente!")

def ventas(request):
    return HttpResponse("Hola ventas!")