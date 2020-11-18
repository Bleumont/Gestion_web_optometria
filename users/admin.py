from django.contrib import admin
from .models import Profesionales, Productos, Pacientes, Turnos, Pedidos
from django.contrib.auth.models import User
# Register your models here.

admin.site.register(Pedidos)
admin.site.register(Turnos)
admin.site.register(Productos)
admin.site.register(Profesionales)
admin.site.register(Pacientes)