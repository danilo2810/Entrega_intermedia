from django.shortcuts import render
from .models import *
from django import forms
from .forms import *

def inicio(request):
    return render (request,'inicio.html')

def personas(request):
    if request.method =='POST':
        miFormulario=PersonaForm(request.POST)
        if miFormulario.is_valid():
            infomacion=miFormulario.cleaned_data
            persona= Persona(nombre_persona=infomacion['nombre_persona'],apellido=infomacion['apellido'],fecha_nacimiento=infomacion['fecha_nacimiento'],dni=infomacion['dni'],email=infomacion['email'])
            persona.save()
            return render(request,"inicio.html",{'mensaje':'Persona cargada correctamente'})
        else:
            return render (request,'personas.html',{'miFormulario': miFormulario })
    else:
        miFormulario=PersonaForm()
        return render (request,'personas.html',{'miFormulario':miFormulario})

def productos(request):
    if request.method =='POST':
        miFormulario=ProductoForm(request.POST)
        if miFormulario.is_valid():
            infomacion=miFormulario.cleaned_data
            producto= Producto(codigo=infomacion['codigo'],fecha_elaboracion=infomacion['fecha_elaboracion'],precio=infomacion['precio'],nombre_producto=infomacion['nombre_producto'],descripcion=infomacion['descripcion'])
            producto.save()
            return render(request,"inicio.html",{'mensaje':'Producto cargado correctamente'})
        else:
            return render (request,'productos.html',{'miFormulario': miFormulario })
    else:
        miFormulario=ProductoForm()
        return render (request,'productos.html',{'miFormulario':miFormulario})

def proveedores(request):
    if request.method =='POST':
        miFormulario=ProveedoresForm(request.POST)
        if miFormulario.is_valid():
            infomacion=miFormulario.cleaned_data
            proveedores= Proveedores(numero_proveedor=infomacion['numero_proveedor'],razon_social=infomacion['razon_social'],inicio_relacion=infomacion['inicio_relacion'],cuit=infomacion['cuit'])
            proveedores.save()
            return render(request,"inicio.html",{'mensaje':'Proveedor cargado correctamente'})
        else:
            return render (request,'proveedores.html',{'miFormulario': miFormulario })
    else:
        miFormulario=ProveedoresForm()
        return render (request,'proveedores.html',{'miFormulario':miFormulario})



def busquedas(request):
    return render(request, 'busquedas.html')

def buscarUsuario(request ):
    nombre=request.GET['nombre']
    if nombre!='':
         nombres=Persona.objects.filter(nombre_persona__icontains=nombre)
         return render(request,"busquedas.html",{'resultado':nombres,'status':1})
    else:
        return render(request,"busquedas.html",{'mensaje':'Campo de búsqueda vacio','status':0})

def buscarProducto(request ):
    nombre=request.GET['nombre']
    if nombre!='':
         nombres=Producto.objects.filter(nombre_producto__icontains=nombre)
         return render(request,"busquedas.html",{'resultado':nombres,'status':2})
    else:
        return render(request,"busquedas.html",{'mensaje':'Campo de búsqueda vacio','status':0})

def buscarProveedor(request ):
    nombre=request.GET['nombre']
    if nombre!='':
         nombres=Proveedores.objects.filter(razon_social__icontains=nombre)
         return render(request,"busquedas.html",{'resultado':nombres,'status':3})
    else:
        return render(request,"busquedas.html",{'mensaje':'Campo de búsqueda vacio','status':0})

def buscarGeneral(request ):
    nombre=request.GET['nombre']
    if nombre!='':

         nombre_provedor=Proveedores.objects.filter(razon_social__icontains=nombre)
         nombre_producto=Producto.objects.filter(nombre_producto__icontains=nombre)
         nombre_persona=Persona.objects.filter(nombre_persona__icontains=nombre)
         return render(request,"busquedas.html",{'nombre_proveedor':nombre_provedor,'nombre_producto':nombre_producto,'nombre_persona':nombre_persona,'status':4})
    else:
        return render(request,"busquedas.html",{'mensaje':'Campo de búsqueda vacio','status':0})