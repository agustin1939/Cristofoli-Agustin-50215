
from django.urls import path, include

from .views import *

urlpatterns = [
    # _______________________________-Urls sin relación con los modelos______________________________________________________________
    
    path("", home, name="home"), # Estoy definiendo que por default al ingresar al servidor me lleve a home
    path('acerca/', acerca, name="acerca_de_mi"), # Página donde se puede ver información personal del autor


    # _______________________________-Urls relacionadas al modelo Servicio __________________________________________________________
    
    path('servicios/', servicios, name="servicios"),
    path('servicio_form/', servicioForm, name="servicio_form"),
    path('servicio_update/<id_servicio>',
         servicioUpdate, name="servicio_update"),
    path('servicio_delete/<id_servicio>',
         servicioDelete, name="servicio_delete"),
    
    # -------------Urls para la búsqueda de servicios a través de letras o palabras clave
    path('buscar_servicios/', buscarServicios, name="buscar_servicios"),
    path('encontrar_servicios/', encontrarServicios, name="encontrar_servicios"),
    
    # _______________________________-Urls relacionadas al modelo Juego __________________________________________________________
    
    path('juegos/', juegos, name="juegos"),
    path('juego_form/', juegoForm, name="juego_form"),
    path('juego_update/<id_juego>', juegoUpdate, name="juego_update"),
    path('juego_delete/<id_juego>', juegoDelete, name="juego_delete"),


    # _______________________________-Urls relacionadas al modelo Consola __________________________________________________________
    
    path('consolas/', ConsolaList.as_view(), name="consolas"),
    path('consola_create/', ConsolaCreate.as_view(), name="consola_create"),
    path('consola_update/<int:pk>/',
         ConsolaUpdate.as_view(), name="consola_update"),
    path('consola_delete/<int:pk>/',
         ConsolaDelete.as_view(), name="consola_delete"),


    # _______________________________-Urls relacionadas al modelo Cliente _________________________________________________________
    
    path('clientes/', ClienteList.as_view(), name="clientes"),
    path('cliente_create/', ClienteCreate.as_view(), name="cliente_create"),
    path('cliente_update/<int:pk>/',
         ClienteUpdate.as_view(), name="cliente_update"),
    path('cliente_delete/<int:pk>/',
         ClienteDelete.as_view(), name="cliente_delete"),

    

    # _______________________________-Urls sobre el login,logout y registro de un usuario ________________________________________

    path('login/', login_request, name="login"),
    path('logout/', logout, name="logout"),
    path('registrar/', register, name="registrar"),

    # _________________________________Urls sobre edición de User, Cambio de clave,________________________________________________
    path('perfil/', editProfile, name="perfil"),
    path("<int:pk>/password/", CambiarClave.as_view(), name="cambiar_clave"),
]
