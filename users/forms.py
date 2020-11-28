from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedidos
        fields = '__all__'

class UpdatePedidoForm(forms.ModelForm):
    class Meta:
        model = Pedidos
        fields = ['estado_pedido']

class TurnoForm(forms.ModelForm):
    class Meta:
        model = Turnos
        fields = '__all__'

class AddTurnoForm(forms.ModelForm):
    class Meta:
        model = Turnos
        fields = ['profesional', 'paciente', 'fecha']

class UpdatePacienteForm(forms.ModelForm):
    class Meta:
        model = Pacientes
        fields = ['historial']

class SearchForm(forms.ModelForm):
    class Meta:
        model = Turnos
        fields = ['fecha']