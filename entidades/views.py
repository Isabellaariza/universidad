from django.shortcuts import render, redirect
from .models import Entidades
from .forms import EntidadesForm, RegistroEntidadForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def registro(request):
    if request.method == 'POST':
        form = RegistroEntidadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroEntidadForm()
    return render(request, 'registro.html', {'form': form})
    
def iniciar_sesion(request):
    if request.method =='POST':
        usuario = request.POST['username']
        clave = request.POST['password']
        user = authenticate(request, username=usuario, password=clave)
        if user:
            login(request, user)
            return redirect('lista_entidades')
        
    return render(request, 'login.html')
        
def cerrar_sesion(request):
    logout(request)
    return redirect('login')

@login_required
def lista_entidades(request):
    entidades = Entidades.objects.all()
    return render(request, 'entidades/lista.html', {'entidades': entidades})

@login_required
def agregar_entidad(request):
    form = EntidadesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_entidades')
    return render(request, 'entidades/form.html', {'form': form})

@login_required
def editar_entidad(request, id):
    entidad = Entidades.objects.get(id=id)
    form = EntidadesForm(request.POST or None, instance=entidad)
    if form.is_valid():
        form.save()
        return redirect('lista_entidades')
    return render(request, 'entidades/form.html', {'form': form})

@login_required
def eliminar_entidad(request, id):
    entidad = Entidades.objects.get(id=id)
    entidad.delete()
    return redirect('lista_entidades')

def generar_reporte_pdf(request):
    entidades = Entidades.objects.all()
    template_path = 'entidades/reporte_pdf.html'
    context = {'entidades': entidades}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte_entidades.pdf"'
    
    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('Hubo un error al generar el PDF', status=500)
    return response

@login_required
def dashboard_entidades(request):
    entidades = Entidades.objects.all()
    nombres = [e.nombre for e in entidades]
    telefonos = [int(e.telefono) for e in entidades]
    return render(request, 'entidades/dashboard.html', {
        'labels': nombres,
        'data': telefonos
    })