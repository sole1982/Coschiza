from django.db import models

class Propiedad(models.Model):
    TIPO_PROPIEDAD_CHOICES = [
        ('casa', 'Casa'),
        ('departamento', 'Departamento'),
        ('ph', 'PH'),
        ('terreno', 'Terreno'),
        ('local', 'Local Comercial'),
        ('oficina', 'Oficina'),
    ]

    ESTADO_PUBLICACION_CHOICES = [
        ('venta', 'En Venta'),
        ('alquiler', 'En Alquiler'),
        ('casa_verano', 'Casa de Verano'),
        ('casa_principal', 'Casa Principal')
    ]

    tipo_propiedad = models.CharField(max_length=20, choices=TIPO_PROPIEDAD_CHOICES, blank=True, null=True   )
    estado_publicacion = models.CharField(max_length=20, choices=ESTADO_PUBLICACION_CHOICES,blank=True, null=True )

    titulo = models.CharField(max_length=200)
    direccion = models.CharField(max_length=255)
    localidad = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(blank=True)
    piso = models.CharField(max_length=50, blank=True, null=True)
    entre_calles = models.CharField(max_length=100, blank=True, null=True)
    unidad = models.CharField(max_length=50, blank=True, null=True)
    cochera_fija = models.BooleanField(default=False)
    orientacion = models.CharField(max_length=50, blank=True, null=True)
    luminosidad = models.CharField(max_length=50, blank=True, null=True)
    amueblado = models.BooleanField(default=False)
    balcon_terraza = models.BooleanField(default=False)
    ubicacion_en_planta = models.CharField(max_length=50, blank=True, null=True)
    estado = models.CharField(max_length=50, default="Muy bueno")
    agua_caliente = models.CharField(max_length=100, default="Termotanque individual")
    superficie_cubierta = models.DecimalField(max_digits=6, decimal_places=2)
    superficie_total = models.DecimalField(max_digits=6, decimal_places=2)
    categoria_edificio = models.CharField(max_length=50, default="Muy Buena")
    cantidad_pisos = models.IntegerField(default=1)
    apto_profesional = models.BooleanField(default=False)
    gas_natural = models.BooleanField(default=False)
    desagues_cloacales = models.BooleanField(default=True)
    pavimento = models.BooleanField(default=True)
    agua_corriente = models.BooleanField(default=True)
    expensas = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    mes_expensas = models.CharField(max_length=50, default="Enero")
    palier = models.CharField(max_length=50, default="Común")
    toilette_recepcion = models.BooleanField(default=False)
    cantidad_banos = models.IntegerField(default=1)
    dormitorio = models.CharField(max_length=50, blank=True, null=True)
    cocina = models.CharField(max_length=50, blank=True, null=True)
  

    def __str__(self):
      return f"{self.titulo} - {self.get_tipo_propiedad_display()} - {self.get_estado_publicacion_display()}"

class ImagenPropiedad(models.Model):
    propiedad = models.ForeignKey(Propiedad, on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.ImageField(upload_to='propiedades/')

    def __str__(self):
        return f"Imagen de {self.propiedad.titulo}"