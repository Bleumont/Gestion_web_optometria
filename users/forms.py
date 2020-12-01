from django import forms
from .models import *


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedidos
        fields = '__all__'

class AddPedidoForm(forms.ModelForm):
    class Meta:
        model = Pedidos
        fields = ['producto', 'cantidad', 'tipo_pago', 'comprador']

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

        widgets = {
            'fecha': forms.SelectDateWidget()
        }

class UpdatePacienteForm(forms.ModelForm):
    class Meta:
        model = Pacientes
        fields = ['historial']

class SearchForm(forms.ModelForm):
    class Meta:
        model = Turnos
        fields = ['fecha']
        widgets = {
            'fecha': forms.SelectDateWidget()
        }

class AddProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = '__all__'
