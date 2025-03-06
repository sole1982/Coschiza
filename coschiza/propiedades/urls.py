from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_propiedades, name='lista_propiedades'),
    path('propiedad/<int:propiedad_id>/', views.detalle_propiedad, name='detalle_propiedad'),
    path('agregar/', views.agregar_propiedad, name='agregar_propiedad'),
    path('tasacion/', views.tasacion, name='tasacion'),
     path('propiedades/', views.listado_propiedades, name='listado_propiedades'),
]
