from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'users/index.html')

def login(request):
    return render(request, 'users/login.html')

def taller(request):
    return HttpResponse("Hola taller!")

def medicos(request):
    return HttpResponse("Hola medico!")

def secretaria(request):
    return HttpResponse("Hola secretaria!")

def gerencia(request):
    return HttpResponse("Hola gerente!")

def ventas(request):
    return HttpResponse("Hola ventas!")