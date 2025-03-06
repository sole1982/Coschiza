from django.shortcuts import render, get_object_or_404, redirect
from .models import Propiedad, ImagenPropiedad
from .forms import PropiedadForm, TasacionForm, ImagenPropiedadForm
from django.core.mail import send_mail

from django.db.models import Q

def lista_propiedades(request):
    tipo = request.GET.get('tipo', None)
    estado = request.GET.get('estado', None)
    casa_principal = Propiedad.objects.filter(estado_publicacion='casa_principal').first() 
    propiedades = Propiedad.objects.all()

    if tipo:
        propiedades = propiedades.filter(tipo_propiedad=tipo)
    
    if estado:
        propiedades = propiedades.filter(estado_publicacion=estado)

    return render(request, 'propiedades/lista.html', {'propiedades': propiedades, 'casa_principal': casa_principal})

def detalle_propiedad(request, propiedad_id):
    propiedad = get_object_or_404(Propiedad, id=propiedad_id)
    return render(request, 'propiedades/detalle.html', {'propiedad': propiedad})



def agregar_propiedad(request):
    if request.method == 'POST':
        form = PropiedadForm(request.POST)
        imagen_form = ImagenPropiedadForm(request.POST, request.FILES)

        if form.is_valid() and imagen_form.is_valid():
            propiedad = form.save()

            for imagen in request.FILES.getlist('imagenes'):
                if imagen:
                    ImagenPropiedad.objects.create(propiedad=propiedad, imagen=imagen)

            return redirect('lista_propiedades')

    else:
        form = PropiedadForm()
        imagen_form = ImagenPropiedadForm()

    return render(request, 'propiedades/agregar.html', {'form': form, 'imagen_form': imagen_form})

def tasacion(request):
    enviado = False
    if request.method == 'POST':
        form = TasacionForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            telefono = form.cleaned_data['telefono']
            mensaje = form.cleaned_data['mensaje']

            # Enviar un correo (requiere configuración de SMTP en settings.py)
            send_mail(
                f'Tasación solicitada por {nombre}',
                f'Email: {email}\nTeléfono: {telefono}\n\nMensaje:\n{mensaje}',
                'tuemail@example.com',  # Cambiar por tu correo
                ['destino@example.com'],  # Cambiar por el correo de destino
            )

            enviado = True
    else:
        form = TasacionForm()

    return render(request, 'propiedades/tasacion.html', {'form': form, 'enviado': enviado})



def listado_propiedades(request):
    tipo = request.GET.get('tipo', '').strip()
    estado = request.GET.get('estado', '').strip()
    
    propiedades = Propiedad.objects.all()
    
    filtros = Q()
    if tipo:
        filtros &= Q(tipo_propiedad=tipo)
    if estado:
        filtros &= Q(estado_publicacion=estado)
    
    propiedades = propiedades.filter(filtros)

    return render(request, 'propiedades/listado_propiedades.html', {'propiedades': propiedades})
