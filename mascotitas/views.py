from django.shortcuts import render, redirect
from .models import *
from .forms import RegistroUserForm, AnimalForm , MercanciaForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from mascotitas.compra import Carrito



def Inicio(request):
    return render(request, 'Inicio.html')

@login_required
def dos(request):
    mascotitas = Animal.objects.raw('Select * from mascotitas_animal')
    datos ={'animalito':mascotitas}
    return render(request, 'dos.html', datos)

def accesperro(request):
    return render(request, 'Acceosrios Perros.html')

def accesgato(request):
    return render(request, 'Accesorios Gatos.html')

def mision(request):
    return render(request, 'Mision.html')

def registro(request):
    return render(request, 'registro.html')

def vet(request):
    return render(request, 'Veterinarios.html')

def adoptar(request):
    return render(request, 'Adoptar.html')

def crear(request):
    return render(request, 'Crear Info.html')


@login_required
def crear(request):
    if request.method=='POST':
        animalform = AnimalForm(request.POST, request.FILES)
        if animalform.is_valid():
            animalform.save()     #similar al insert en función
            return redirect('dos')
    else:
        animalform=AnimalForm()
    return render(request, 'Crear Info.html',{'animalform': animalform})

@login_required
def eliminar(request, id):
    animalEliminado=Animal.objects.get(nombre=id)  #obtenemos un objeto por su pk
    animalEliminado.delete()
    return redirect('dos')

@login_required
def modificar(request,id):
    animal = Animal.objects.get(nombre=id)         #obtenemos un objeto por su pk
    datos ={
        'form':AnimalForm(instance=animal)
    }
    if request.method=='POST':
        formulario = AnimalForm(data=request.POST, instance=animal)
        if formulario.is_valid:
            formulario.save()
            return redirect ('dos')
    return render(request, 'modificar.html', datos)





#método que permite registrar un usuario
def registrar(request):
    data = {
        'form' : RegistroUserForm()         #creamos un objeto de tipo forms para user
    }
    if request.method=="POST":
        formulario = RegistroUserForm(data = request.POST)  
        if formulario.is_valid():
            formulario.save()
            user= authenticate(username=formulario.cleaned_data["username"],
                  password=formulario.cleaned_data["password1"])
            login(request,user)   
            return redirect('Inicio')
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)


def adoptar(request):
    animalito = Animal.objects.all()
    datos={
        'animalito': animalito
    }
    return render(request,'Adoptar.html',datos)


def carrito(request):
    return render(request, 'carrito.html')

def tienda(request):
    articulo = Mercancia.objects.all()
    datos={
        'articulo':articulo
    }
    return render(request, 'tienda.html', datos)


def agregar_producto(request,id):
    carrito_compra= Carrito(request)
    articulo = Mercancia.objects.get(nombre=id)
    carrito_compra.agregar(articulo=articulo)
    return redirect('tienda')

def eliminar_producto(request, id):
    carrito_compra= Carrito(request)
    articulo = Mercancia.objects.get(nombre=id)
    carrito_compra.eliminar(articulo=articulo)
    return redirect('tienda')

def restar_producto(request, id):
    carrito_compra= Carrito(request)
    articulo = Mercancia.objects.get(nombre=id)
    carrito_compra.restar(articulo=articulo)
    return redirect('tienda')

def limpiar_carrito(request):
    carrito_compra= Carrito(request)
    carrito_compra.limpiar()
    return redirect('tienda') 
   
def total_carrito(request,precio):
    carrito_compra= Carrito(request)
    precio = Mercancia.objects.get(precio=precio)
    carrito_compra.total_c(precio=precio)
    return redirect('tienda')

def total_carrito_imp(request,precio):
    carrito_compra= Carrito(request)
    precio = Mercancia.objects.get(precio=precio)
    carrito_compra.total_c(precio=precio)
    return redirect('tienda') 

def generarBoleta(request):
    for key, value in request.session['carrito'].items():
        articulo = Mercancia.objects.get(nombre=value['mercancia_id'])
        cantidad = value['cantidad']
        descontar_stock(articulo.nombre, cantidad)

    precio_total=0
    precio_total_t=0
    envio=2000
    precio_total_imp = 0  

    for key, value in request.session['carrito'].items():
        precio_total = precio_total + int(value['precio']) * int(value['cantidad'])
        precio_total_imp = precio_total*0.19
    precio_total_t= precio_total+envio
    usuario_actual = request.user
    boleta = Boleta(total_imp = precio_total_imp , total = precio_total_t , usuario=usuario_actual)
    boleta.save()
    productos = []
    for key, value in request.session['carrito'].items():
            producto = Mercancia.objects.get(nombre = value['mercancia_id'])
            cant = value['cantidad']
            subtotal = cant * int(value['precio'])
            subtotal_imp = subtotal * 0.19
            detalle = detalle_boleta(id_boleta = boleta, id_producto = producto, cantidad = cant, subtotal = subtotal, subtotal_imp = subtotal_imp )
            detalle.save()
            productos.append(detalle)
    datos={
        'usuario': boleta.usuario,
        'productos':productos,
        'fecha':boleta.fechaCompra,
        'envio' : boleta.envio, 
        'total_imp' :boleta.total_imp,
        'total': boleta.total
    }
    request.session['boleta'] = boleta.id_boleta
    carrito = Carrito(request)
    carrito.limpiar()
    return render(request, 'detallecarrito.html',datos)

def descontar_stock(articulo_nombre, cantidad):
    try:
        articulo = Mercancia.objects.get(nombre=articulo_nombre)
        if articulo.stock >= cantidad:
            articulo.stock -= cantidad
            articulo.save()
            return True
        else:
            return False
    except Mercancia.DoesNotExist:
        return False
    

