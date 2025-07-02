"""tienda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from entidades import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.iniciar_sesion, name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('entidades/', views.lista_entidades, name='lista_entidades'),
    path('entidad/agregar/', views.agregar_entidad, name='agregar_entidad'),
    path('entidad/editar/<int:id>/', views.editar_entidad, name='editar_entidad'),
    path('entidad/eliminar/<int:id>/', views.eliminar_entidad, name='eliminar_entidad'),
    path('entidades/reporte/pdf/', views.generar_reporte_pdf, name='reporte_pdf'),
    path('entidades/dashboard/', views.dashboard_entidades, name='dashboard_entidades'),
]