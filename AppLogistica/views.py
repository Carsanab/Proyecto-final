from django.shortcuts import render
from AppLogistica.models import*
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import admin,authenticate,login
from AppLogistica.forms import registroformulario


# Create your views here.

def inicio(request):
  mensaje="Bienvenidos a la Plataforma"
  return  render(request,'AppLogistica/inicio.html',{"mensaje":mensaje})

    


def registro(request):

    if request.method == "POST":
        miformulario=registroformulario(request.POST) # obtener los datos del formulario

        if miformulario.is_valid():
            miformulario.save()
            return render(request,"AppLogistica/inicio.html")
        
    else:
        miformulario=registroformulario()

    return render(request,"AppLogistica/autenticacion/registro.html",{"miformulario":miformulario})

  
def iniciar_sesion(request):

    if request.method == "POST":
        formulario=AuthenticationForm(request,data = request.POST) #Obtener los datos del formulario

        if formulario.is_valid():
            usuario=formulario.cleaned_data.get("username")
            contra=formulario.cleaned_data.get("password")
            
            miusuario=authenticate(username=usuario,password=contra)

            if miusuario:
                login(request,miusuario)
                mensaje= f"Bienvenido a la Plataforma {miusuario}"
                return render(request,"AppLogistica/inicio.html",{"mensaje":mensaje})

        else:
            mensaje= f"Error al ingresar los datos"
            return render(request,"AppLogistica/inicio.html",{"mensaje":mensaje})  

    else:
        formulario=AuthenticationForm()

    return render(request,"AppLogistica/autenticacion/login.html",{"formulario":formulario})    

#Creación de CRUD usando clases

# Ver choferes, Crear uno nuevo, Editar, Eliminar
class lista_proveedores(ListView):
    model=proveedor

class detalle_proveedores(DetailView):
    model=proveedor    

class crear_proveedor(CreateView):
    model=proveedor
    success_url='/AppLog/proveedor/list'
    fields=['cuit','razon_social','telefono','Correo']

class editar_proveedor(UpdateView):
    model=proveedor
    success_url='/AppLog/proveedor/list'
    fields=['cuit','razon_social','telefono','Correo']

class eliminar_proveedor(DeleteView):
    model=proveedor
    success_url='/AppLog/proveedor/list'





# Ver Clientes, Crear uno nuevo, Editar, Eliminar
class lista_clientes(ListView):
    model=cliente

class crear_cliente(CreateView):
    model=cliente
    success_url='/AppLog/cliente/list'
    fields=['cuit','razon_social','telefono','Correo']

class editar_cliente(UpdateView):
    model=cliente
    success_url='/AppLog/cliente/list'
    fields=['cuit','razon_social','telefono','Correo']

class eliminar_cliente(DeleteView):
    model=cliente
    success_url='/AppLog/cliente/list'

    

# Ver Choferes, Crear uno nuevo, Editar, Eliminar
class lista_choferes(ListView):
    model=chofer

class detalle_choferes(DetailView):
    model=chofer    

class crear_chofer(CreateView):
    model=chofer
    success_url='/AppLog/chofer/list'
    fields=['nombre','dni','vto_licencia','vto_linti']

class editar_chofer(UpdateView):
    model=chofer
    success_url='/AppLog/chofer/list'
    fields=['nombre','dni','vto_licencia','vto_linti']

class eliminar_chofer(DeleteView):
    model=chofer
    success_url='/AppLog/chofer/list'


# Ver Unidades, Crear uno nuevo, Editar, Eliminar
class lista_unidades(ListView):
    model=unidad

class detalle_unidades(DetailView):
    model=unidad    

class crear_unidad(CreateView):
    model=unidad
    success_url='/AppLog/unidad/list'
    fields=['patente','tipo','vto_vtv','vto_ruta']

class editar_unidad(UpdateView):
    model=unidad
    success_url='/AppLog/unidad/list'
    fields=['patente','tipo','vto_vtv','vto_ruta']

class eliminar_unidad(DeleteView):
    model=unidad
    success_url='/AppLog/unidad/list'




#Ver Cargas, Crear uno nuevo, Editar, Eliminar
class lista_cargas(ListView):
    model=carga

class crear_carga(CreateView):
    model=carga
    success_url='/AppLog/carga/list'
    fields=['fecha','origen','destino','tipo_carga','cantidad']

class editar_carga(UpdateView):
    model=carga
    success_url='/AppLog/carga/list'
    fields=['fecha','origen','destino','tipo_carga','cantidad']

class eliminar_carga(DeleteView):
    model=carga
    success_url='/AppLog/carga/list'