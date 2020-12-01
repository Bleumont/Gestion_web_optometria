"""clinica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('', views.landing, name='landing'),
    path('landing/', views.index, name='index'),
    path('secretaria/', views.secretaria, name='secretaria'),
    path('medicos/', views.medicos, name='medicos'),
    path('taller/', views.taller, name='taller'),
    path('update_pedido/<str:p_key>/', views.update_pedido, name='update_pedido'),
    path('update_turno/<str:t_key>/', views.update_turno, name='update_turno'),
    path('del_turno/<str:t_key>/', views.del_turno, name='del_turno'),
    path('update_paciente/<str:p_key>/', views.update_paciente, name='update_paciente'),
    path('update_venta/<str:p_key>/', views.update_venta, name='update_venta'),
    path('update_producto/<str:p_key>/', views.update_producto, name='update_producto'),
    path('add_turno/', views.add_turno, name='add_turno'),
    path('add_producto/', views.add_producto, name='add_producto'),
    path('add_pedido/', views.add_pedido, name='add_pedido'),
    path('gerencia/', views.gerencia, name='gerencia'),
    path('ventas/', views.ventas, name='ventas'),
    path('403/', views.unauthorized, name='403'),
]
