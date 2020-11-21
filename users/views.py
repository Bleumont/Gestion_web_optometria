from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pacientes, Pedidos, Productos, Profesionales, Turnos
from django.contrib.auth import authenticate, login, logout
from .decorators import allowed_users, unauthenticated_user, admin_only
from django.contrib.auth.decorators import login_required



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

@login_required(login_url='login')
@allowed_users(allowed_roles=['Secretaria','admin','Gerencia'])
def secretaria(request):
    return render(request, 'users/secretaria.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['Taller','admin','Gerencia'])
def taller(request):
    return render(request, 'users/taller.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['Gerencia','admin','Gerencia'])
def gerencia(request):
    return render(request, 'users/gerencia.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['Ventas','admin','Gerencia'])
def ventas(request):
    return render(request, 'users/ventas.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['Profesionales','admin','Gerencia'])
def medicos(request):
    return render(request, 'users/medicos.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['Profesionales','admin','Gerencia', 'Profesionales', 'Ventas', 'Taller', 'Secretaria'])
def management(request):
    return render(request, 'users/management.html')

def unauthorized(request):
    return render(request, 'users/403.html')

def notfound(request):
    return render(request, 'users/404.html')