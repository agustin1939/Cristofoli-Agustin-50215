from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Servicio, Juego, Consola, Cliente
from .forms import ServicioForm, JuegoForm, RegistroForm, UserEditForm, User
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import logout as django_logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# ___________________________________________Funciones adicionales__________________________________________________________________________________


def home(request):
    # Renderiza la página "index.html" en la vista home
    return render(request, "aplicacion4/index.html")


def acerca(request):
    # Renderiza la página "acerca.html" en la vista acerca
    return render(request, "aplicacion4/acerca.html")

# ___________________________________________Servicios__________________________________________________________________________________


def servicios(request):  # Función utilizada para mostrar los objetos del modelo Servicio
    # Obtener todos los objetos de Servicio ordenados por orden predeterminado
    contexto = {'servicios': Servicio.objects.all().order_by()}
    # Renderizar la página "servicios.html" con todos los servicios
    return render(request, "aplicacion4/servicios.html", contexto)


@login_required  # Solo usuarios autenticados pueden acceder a la vista
def servicioForm(request):  # Función utilizada para crear objetos del modelo Servicio
    if request.method == "POST":  # Estoy analizando si es la segunda o enesima vez que entra al formulario, si es la primera vez crea un formulario, vacío, es decir me dirige al else, y luego a return que envia el formulario vacio al html
        miForm = ServicioForm(request.POST)
        if miForm. is_valid():  # Si estos datos son validos voy a tomar nombre y tiempo , lo hago a traves del metodo de abajo
            servicio_nombre = miForm.cleaned_data.get("nombre")
            servicio_tiempo = miForm.cleaned_data.get("tiempo")
            servicio = Servicio(nombre=servicio_nombre, tiempo=servicio_tiempo)
            servicio.save()  # Guardar los datos
            contexto = {'servicios': Servicio.objects.all()}
            # Retornar el control a la pagina principal de la aplicacionhtml
            return render(request, "aplicacion4/servicios.html", contexto)
    else:  # Es la primera vez que me esta haciendo la peticion

        miForm = ServicioForm()
    return render(request, "aplicacion4/servicioForm.html", {"form": miForm})


@login_required  # Solo usuarios autenticados pueden acceder a la vista
# Función utilizada para actualizar objetos del modelo Servicio
def servicioUpdate(request, id_servicio):
    # Obtener el servicio a actualizar
    servicio = Servicio.objects.get(id=id_servicio)

    # Si la solicitud es un POST (envío de formulario)
    if request.method == "POST":
        # Crear el formulario ServicioForm con los datos enviados y el servicio actual
        miForm = ServicioForm(request.POST, instance=servicio)
        if miForm.is_valid():  # Verificar si el formulario es válido
            miForm.save()  # Guardar los cambios actualizados en la base de datos
            # Obtener todos los servicios actualizados
            contexto = {'servicios': Servicio.objects.all()}
            # Redirigir a la página de servicios con la lista actualizada
            return render(request, "aplicacion4/servicios.html", contexto)
    # Si la solicitud no es un POST (primera vez que se carga la página o se envía un formulario vacío)
    else:
        # Crear un formulario ServicioForm con los datos actuales del servicio para editarlos
        miForm = ServicioForm(instance=servicio)

    # Renderizar el formulario ServicioForm
    return render(request, "aplicacion4/servicioForm.html", {"form": miForm})


@login_required  # Solo usuarios autenticados pueden acceder a la vista
# Función utilizada para eliminar objetos del modelo Servicio
def servicioDelete(request, id_servicio):
    # Obtener el servicio a eliminar utilizando su id
    servicio = Servicio.objects.get(id=id_servicio)
    servicio.delete()  # Eliminar el servicio de la base de datos
    # Redirigir a la URL de la lista de servicios ('servicios')
    return redirect(reverse_lazy('servicios'))

# ------------------------------------------  Busqueda de servicios---------------------------------------------


@login_required  # Solo usuarios autenticados pueden acceder a la vista
def buscarServicios(request):
    # Renderiza la página "buscar.html" para buscar servicios
    return render(request, "aplicacion4/buscar.html")


@login_required
def encontrarServicios(request):
    # Verificar si existe un parámetro 'buscar' en la solicitud GET y no está vacío
    if request.GET.get("buscar"):
        # Obtener el valor del parámetro 'buscar' de la solicitud GET
        patron = request.GET["buscar"]
        # Filtrar todos los objetos de Servicio que contienen el patrón en el nombre (caso insensible a mayúsculas y minúsculas)
        servicios = Servicio.objects.filter(nombre__icontains=patron)
        # Crear un contexto con los servicios filtrados
        contexto = {"servicios": servicios}
        # Renderizar la página "servicios.html" con el contexto filtrado
        return render(request, "aplicacion4/servicios.html", contexto)

    # Si no se proporcionó un parámetro 'buscar' o está vacío, mostrar todos los servicios
    # Obtener todos los objetos de Servicio
    contexto = {'servicios': Servicio.objects.all()}
    # Renderizar la página "servicios.html" con todos los servicios
    return render(request, "aplicacion4/servicios.html", contexto)

# ___________________________________________________Juegos______________________________________________________________________________


def juegos(request):  # Función utilizada para mostrar los objetos del modelo Juego
    # Crear un contexto con todos los juegos disponibles
    contexto = {'juegos': Juego.objects.all()}
    # Renderizar la página de juegos con el contexto
    return render(request, "aplicacion4/juegos.html", contexto)


@login_required  # Solo usuarios autenticados pueden acceder a la vista
def juegoForm(request):  # Función utilizada para crear objetos del modelo Juego
    # Si la solicitud es un POST (envío de formulario)
    if request.method == "POST":
        # Crear el formulario JuegoForm con los datos enviados
        miForm = JuegoForm(request.POST)
        if miForm.is_valid():  # Verificar si el formulario es válido
            # Obtener el nombre del juego del formulario
            juego_nombre = miForm.cleaned_data.get("nombre")
            # Obtener la consola del juego del formulario
            juego_consola = miForm.cleaned_data.get("consola")
            # Obtener el stock del juego del formulario
            juego_stock = miForm.cleaned_data.get("stock")
            # Crear una instancia del modelo Juego
            juego = Juego(nombre=juego_nombre,
                          consola=juego_consola, stock=juego_stock)
            juego.save()  # Guardar el juego en la base de datos
            # Redirigir a la URL de la lista de juegos
            return redirect('juegos')
    else:  # Si la solicitud no es un POST (primera vez que se carga la página)
        miForm = JuegoForm()  # Crear un formulario JuegoForm vacío
    # Renderizar el formulario JuegoForm
    return render(request, "aplicacion4/juegosForm.html", {"form": miForm})


@login_required  # Solo usuarios autenticados pueden acceder a la vista
# Función utilizada para actualizar objetos del modelo Juego
def juegoUpdate(request, id_juego):
    juego = Juego.objects.get(id=id_juego)  # Obtener el juego a actualizar
    # Si la solicitud es un POST (envío de formulario)
    if request.method == "POST":
        # Crear el formulario JuegoForm con los datos enviados
        miForm = JuegoForm(request.POST)
        if miForm.is_valid():  # Verificar si el formulario es válido
            # Actualizar el nombre del juego en el objeto Juego
            juego.nombre = miForm.cleaned_data.get("nombre")
            # Actualizar la consola del juego en el objeto Juego
            juego.consola = miForm.cleaned_data.get("consola")
            # Actualizar el stock del juego en el objeto Juego
            juego.stock = miForm.cleaned_data.get("stock")
            juego.save()  # Guardar los cambios actualizados en la base de datos
            # Obtener todos los juegos actualizados
            contexto = {'juegos': Juego.objects.all().order_by("id")}
            # Redirigir a la página de juegos con la lista actualizada
            return render(request, "aplicacion4/juegos.html", contexto)
    # Si la solicitud no es un POST (primera vez que se carga la página o se envía un formulario vacío)
    else:
        # Crear un formulario JuegoForm con los datos actuales del juego para editarlos
        miForm = JuegoForm(
            initial={'nombre': juego.nombre, 'consola': juego.consola, 'stock': juego.stock})

    # Renderizar el formulario JuegoForm
    return render(request, "aplicacion4/juegosForm.html", {"form": miForm})


@login_required  # Solo usuarios autenticados pueden acceder a la vista
def juegoDelete(request, id_juego):  # Función utilizada para eliminar  objetos del modelo Juego
    # Obtener el juego a eliminar utilizando su id
    juego = Juego.objects.get(id=id_juego)
    juego.delete()  # Eliminar el juego de la base de datos
    # Redirigir a la URL de la lista de juegos ('juegos')
    return redirect(reverse_lazy('juegos'))


# _________________________________________________Consolas_____________________________________________________________________________
class ConsolaList(ListView):  # Esta clase se utiliza para mostrar los objetos Consola
    model = Consola


# Esta clase se utiliza para crear objetos Consola, solo usuarios autenticados pueden acceder a la vista
class ConsolaCreate(LoginRequiredMixin, CreateView):
    model = Consola
    fields = ["nombre", "año", "estado", "stock"]
    success_url = reverse_lazy("consolas")


# Esta clase se utiliza para editar objetos Consola, solo usuarios autenticados pueden acceder a la vistaa
class ConsolaUpdate(LoginRequiredMixin, UpdateView):
    model = Consola
    fields = ["nombre", "año", "estado", "stock"]
    success_url = reverse_lazy("consolas")


# Esta clase se utiliza para eliminar objetos Consola, solo usuarios autenticados pueden acceder a la vista
class ConsolaDelete(LoginRequiredMixin, DeleteView):
    model = Consola
    fields = ["nombre", "año", "estado", "stock"]
    success_url = reverse_lazy("consolas")


# ________________________________________________Clientes_____________________________________________________________________________

class ClienteList(LoginRequiredMixin,ListView):  # Esta clase se utiliza para mostrar los objetos Cliente
    model = Cliente


# Esta clase se utiliza para crear objetos Cliente, solo usuarios autenticados pueden acceder a la vista
class ClienteCreate(LoginRequiredMixin, CreateView):
    model = Cliente
    fields = ["nombre", "apellido", "email"]
    success_url = reverse_lazy("clientes")


# Esta clase se utiliza para actualizar los objetos Cliente, solo usuarios autenticados pueden acceder a la vista
class ClienteUpdate(LoginRequiredMixin, UpdateView):
    model = Cliente
    fields = ["nombre", "apellido", "email"]
    success_url = reverse_lazy("clientes")


# Esta clase se utiliza para eliminar objetos Cliente, solo usuarios autenticados pueden acceder a la vista
class ClienteDelete(LoginRequiredMixin, DeleteView):
    model = Cliente
    fields = ["nombre", "apellido", "email"]
    success_url = reverse_lazy("clientes")


# ______________________________________________________Login_____________________________________________________________________________

def login_request(request):  # Función utilizada para el inicio de sesión de usuarios
    # Si la solicitud es un POST (envío de formulario)
    if request.method == "POST":
        # Obtener el nombre de usuario del formulario
        usuario = request.POST['username']
        # Obtener la contraseña del formulario
        clave = request.POST['password']
        user = authenticate(request, username=usuario,
                            password=clave)  # Autenticar el usuario
        if user is not None:  # Si la autenticación es exitosa
            login(request, user)  # Iniciar sesión para el usuario autenticado
            # Renderizar la página de inicio
            return render(request, "aplicacion4/index.html")
        else:  # Si la autenticación falla
            # Redireccionar al formulario de inicio de sesión
            return redirect(reverse_lazy('login'))
    else:  # Si la solicitud no es un POST (primera vez que se carga la página)
        miForm = AuthenticationForm()  # Crear un formulario de autenticación vacío
        # Renderizar el formulario de inicio de sesión
        return render(request, "aplicacion4/login.html", {"form": miForm})

# ______________________________________________________Logout_____________________________________________________________________________


def logout(request):  # Función utilizada para el cierre de sesión de usuarios
    # Si la solicitud es un POST (envío de formulario de logout)
    if request.method == 'POST':
        django_logout(request)  # Cerrar la sesión del usuario
        return redirect('home')  # Redireccionar a la página de inicio ('home')
    else:  # Si la solicitud no es un POST (carga normal de la página de logout)
        # Renderizar la página de logout
        return render(request, 'aplicacion4/logout.html')

# ______________________________________________________Register_____________________________________________________________________________


def register(request):  # Función utilizada para el registro de usuarios
    # Si la solicitud es un POST (envío de formulario de registro)
    if request.method == "POST":
        # Crear el formulario de registro con los datos enviados
        miForm = RegistroForm(request.POST)

        if miForm.is_valid():  # Verificar si el formulario es válido
            # Obtener el nombre de usuario del formulario
            usuario = miForm.cleaned_data.get("username")
            miForm.save()  # Guardar el nuevo usuario en la base de datos
            # Redireccionar a la página de inicio ('home')
            return redirect(reverse_lazy('home'))
    # Si la solicitud no es un POST (primera vez que se carga la página de registro)
    else:
        miForm = RegistroForm()  # Crear un formulario de registro vacío

    # Renderizar el formulario de registro
    return render(request, "aplicacion4/registro.html", {"form": miForm})


# ___________________________________________________Edicion de User______________________________________________________________________

@login_required  # Solo usuarios autenticados pueden acceder a la vista
def editProfile(request):
    usuario = request.user  # Crea un objeto usuario leyendo el usuario de la base de datos
    if request.method == "POST":
        # Si el usuario ya modifico sus datos creamos un formulario
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():  # Si el formulario es válido vamos a obtener todos los datos
            user = User.objects.get(username=usuario)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()  # Guarda el usuario actualizando los datos del mismo en la base de datos
            return redirect(reverse_lazy('home'))  # Retornamos a home
    else:
        # __ Si ingresa en el else es la primera vez  recuperamos los datos del usuario que llegan por el request
        miForm = UserEditForm(instance=usuario)

    # Renderizar el formulario de edición de perfil
    return render(request, "aplicacion4/editarPerfil.html", {"form": miForm})

# ___________________________________________________Cambio de Clave______________________________________________________________________


# Vista para cambiar la contraseña del usuario
class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    # Template utilizado para mostrar el formulario de cambio de contraseña
    template_name = "aplicacion4/cambiar_clave.html"
    # Se redirige a home  después de cambiar la contraseña
    success_url = reverse_lazy("home")
