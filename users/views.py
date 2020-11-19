from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pacientes, Pedidos, Productos, Profesionales, Turnos
from django.contrib.auth import authenticate, login, logout



profes = {
    'nombre': Profesionales.nombre,
    'dni': Profesionales.dni
}

# Create your views here.
def index(request):
    return render(request, 'users/index.html')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, username)
            redirect('index')
    else: 
        return render(request, 'users/login.html', )

def logoutUser(request):
    logout(request)
    return redirect('logout')
 