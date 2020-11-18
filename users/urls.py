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
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('secretaria/', views.secretaria, name='area-secretaria'),
    path('medicos/', views.medicos, name='area-medicos'),
    path('gerencia/', views.gerencia, name='gerencia'),
    path('ventas/', views.ventas, name='area-ventas'),
    path('taller/', views.taller, name='area-taller'),
    path('management/', views.management, name='management'),
]
