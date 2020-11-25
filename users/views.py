from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users, unauthenticated_user, admin_only
from .models import Pedidos, Pacientes, Profesionales, Turnos, Productos
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'users/index.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['Profesionales','admin','Gerencia', 'Profesionales',
'Ventas', 'Taller', 'Secretaria'])
def dashboard(request):
    return render(request, 'users/dashboard.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, username)
            redirect('dashboard')
    else:
        return render(request, 'users/login.html', )

def logout_user(request):
    logout(request)
    return redirect('logout')

@login_required(login_url='login')
@allowed_users(allowed_roles=['Secretaria','admin','Gerencia'])
def secretaria(request):
    turnos = Turnos.objects.all()
    context = {'turnos': turnos}

    return render(request, 'users/secretaria.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Secretaria','admin','Gerencia'])
def add_turno(request):
    
    form = AddTurnoForm(request.POST)
    if request.method == 'POST':
        form = AddTurnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('secretaria')

    return render(request, 'users/add_turno.html', {'form': form})

@login_required(login_url='login')
@allowed_users(allowed_roles=['Secretaria','admin','Gerencia'])
def del_turno(request, t_key):
    turno = Turnos.objects.get(id=t_key)
    
    if request.method == 'POST':
        turno.delete()
        return redirect('secretaria')

    return render(request, 'users/del_turno.html', {'turno': turno})

@login_required(login_url='login')
@allowed_users(allowed_roles=['Taller','admin','Gerencia'])
def taller(request):
    pedidos = Pedidos.objects.all()
    context = {'Pedidos': pedidos}

    return render(request, 'users/taller.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Gerencia','admin','Gerencia'])
def gerencia(request):
    pedidos = Pedidos.objects.all()
    pacientes = Pacientes.objects.all()
    medicos = Profesionales.objects.all()
    turnos = Turnos.objects.all()
    productos = Productos.objects.all()

    total_pedidos = pedidos.count()
    entregados = pedidos.filter(estado_pedido='Finalizado').count()
    pendientes = pedidos.filter(estado_pedido='Pendiente').count()
    asistencias = turnos.filter(asistencia=True).count()
    asistencias = turnos.filter(asistencia=False).count()
    pedidos_por_paciente= pedidos.filter(published_date__lte=timezone.now())
    context = {'Pedidos': pedidos, 'Pacientes': pacientes, 'Pedidos Totales': total_pedidos,
    'Entregados': entregados, 'Pendientes': pendientes, 'Turnos': turnos, 'Productos': productos, 'Profesionales': medicos}

    return render(request, 'users/gerencia.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Ventas','admin','Gerencia'])
def ventas(request):
    return render(request, 'users/ventas.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['Profesionales','admin','Gerencia'])
def medicos(request):
    pacientes = Pacientes.objects.all()
    context = {'pacientes': pacientes}

    return render(request, 'users/medicos.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Profesionales','admin','Gerencia'])
def update_paciente(request, p_key):
    paciente = Pacientes.objects.get(id=p_key)
    form = UpdatePacienteForm(instance=paciente)
    context = {'paciente': paciente, 'form': form}
    if request.method == 'POST':
        form = UpdatePacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('medicos')

    return render(request, 'users/update_paciente.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Taller','admin'])
def update_pedido(request, p_key):
    pedido = Pedidos.objects.get(id=p_key)
    form = UpdatePedidoForm(instance=pedido)
    
    context = {'pedido': pedido, 'form': form}

    if request.method == 'POST':
        form = UpdatePedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('taller')

    return render(request, 'users/update_pedido.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Secretaria','admin'])
def update_turno(request, t_key):
    turno = Turnos.objects.get(id=t_key)
    form = TurnoForm(instance=turno)
    
    context = {'turno': turno, 'form': form}

    if request.method == 'POST':
        form = TurnoForm(request.POST, instance=turno)
        if form.is_valid():
            form.save()
            return redirect('secretaria')

    return render(request, 'users/update_turno.html', context)

def unauthorized(request):
    return render(request, 'users/403.html')

def notfound(request):
    return render(request, 'users/404.html')
