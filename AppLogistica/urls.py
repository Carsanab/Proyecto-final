from django.urls import path
from AppLogistica.views import*
from django.http import HttpResponse
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('Inicio/',inicio,name="iniciar"),
    

    #url para el registro
    path('registro/',registro,name='registrar'),
    #url para inicio de sesión
    path('login/',iniciar_sesion,name='entrar'),
    
    path('logout/',LogoutView.as_view(template_name="AppLogistica/autenticacion/logout.html"),name="salir"),

    path('proveedor/list/',lista_proveedores.as_view(),name='proveedores_lista'),
    path('proveedor/crear',crear_proveedor.as_view(),name='proveedor_crear'),
    path('proveedor/editar/<int:pk>',editar_proveedor.as_view(),name='proveedor_editar'),
    path('proveedor/eliminar/<int:pk>',eliminar_proveedor.as_view(),name='proveedor_eliminar'),

    path('cliente/list/',lista_clientes.as_view(),name='clientes_lista'),
    path('cliente/crear',crear_cliente.as_view(),name='cliente_crear'),
    path('cliente/editar/<int:pk>',editar_cliente.as_view(),name='cliente_editar'),
    path('cliente/eliminar/<int:pk>',eliminar_cliente.as_view(),name='cliente_eliminar'),

    path('chofer/list/',lista_choferes.as_view(),name='choferes_lista'),
    path('chofer/crear',crear_chofer.as_view(),name='chofer_crear'),
    path('chofer/editar/<int:pk>',editar_chofer.as_view(),name='chofer_editar'),
    path('chofer/eliminar/<int:pk>',eliminar_chofer.as_view(),name='chofer_eliminar'),

    path('unidad/list/',lista_unidades.as_view(),name='unidades_lista'),
    path('unidad/crear',crear_unidad.as_view(),name='unidad_crear'),
    path('unidad/editar/<int:pk>',editar_unidad.as_view(),name='unidad_editar'),
    path('unidad/eliminar/<int:pk>',eliminar_unidad.as_view(),name='unidad_eliminar'),

    path('carga/list/',lista_cargas.as_view(),name='cargas_lista'),
    path('carga/crear',crear_carga.as_view(),name='carga_crear'),
    path('carga/editar/<int:pk>',editar_carga.as_view(),name='carga_editar'),
    path('carga/eliminar/<int:pk>',eliminar_carga.as_view(),name='carga_eliminar'),


    
]