from django.shortcuts import  render, redirect
from carts.models import CartItem ,Cart
from carts.views import _cart_id, checkout
from orders.models import Order, OrderProduct
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import User
from . models import *
from .models import SubCategoria, Categoria
from django.core.paginator import EmptyPage, PageNotAnInteger,Paginator
from django.contrib.auth.decorators import login_required, permission_required
from carts.views import _cart_id
from .serializers import ProductoSerializer
from rest_framework import viewsets


class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer



def home (request):
    productos = Producto.objects.all().filter(is_available=True)
    categorias = Categoria.objects.all()
    SubCat = SubCategoria.objects.all()

    context = {'productos': productos,'categorias':categorias}
    return render(request, 'app/home.html', context)


def CrearUsuario(request):
    data = { 'form' : RegistroEmp()}
    if request.method == 'POST':
        formulario = RegistroEmp(data= request.POST)
        if formulario.is_valid():
            tipo = formulario.cleaned_data["tipo"]
            email = formulario.cleaned_data["email"]
            username= formulario.cleaned_data["username"]
            apellido= formulario.cleaned_data["apellido"]
            telefono= formulario.cleaned_data["telefono"]
            password = formulario.cleaned_data["password"]
            # funcion que llama al manager custom de user para crear un usuario bodeguero, revisar models customuser
            if tipo == 'bodeguero' :
                User.objects.create_bodeguero(email,username,apellido,password,telefono) 
            elif tipo == 'vendedor':
                 User.objects.create_vendedor(email,username,apellido,password,telefono) 
            elif tipo == 'contador':
                User.objects.create_contador(email,username,apellido,password,telefono) 
            else:
                pass
            messages.success(request, 'Colaborador Registrado Correctamente')
            return redirect(to='CrearUsuario')
        
        data["form"] = formulario
          
    return render(request, 'registration/registro.html', data)

def adminView (request):
    return render(request, 'app/admini/vistaAdmin.html')


def loginCli (request):
    data = { 'form' : LoginCli()}
    if request.method == 'POST':
        formulario = LoginCli(data= request.POST)
        if formulario.is_valid():
            user = authenticate(username= formulario.cleaned_data["email"],password= formulario.cleaned_data['contrasena'])
            if user is not None:
                try:
                    cart = Cart.objects.get(cart_id=_cart_id(request))
                    is_cart_item_exist = CartItem.objects.filter(cart=cart).exists()
                    if is_cart_item_exist:
                        cart_item = CartItem.objects.filter(cart=cart)
                        for item in cart_item:
                            item.user = user
                            item.save()
                except:
                    pass

                login(request,user)
                return redirect(to='home')
            else :
                pass #Falta ponner mensaje de alerta o similar
        data["form"] = formulario
        
    return render(request, 'app/loguinCli.html',data)

def RegistroCli (request):
    
    if request.method == 'GET':
       data = { 'form' : RegistroClie()}
       return render(request, 'registration/registroCli.html',data)
    
    else:
        if request.method == 'POST':
            formulario = RegistroClie(data= request.POST)
            if formulario.is_valid():
                email = formulario.cleaned_data["email"]
                username= formulario.cleaned_data["username"]
                apellido= formulario.cleaned_data["apellido"]
                telefono= formulario.cleaned_data["telefono"]
                password = formulario.cleaned_data["password"]
                User.objects.create_user(email,username,apellido,password,telefono) 
                messages.success(request, "Te has registrado corectamente")

                return redirect(to='home')
            data["form"] = formulario
    return render(request, 'registration/registroCli.html',data)




def store (request, slug):

    tipo = None
    catslug = Categoria.objects.get(slug = slug)
    subcat = SubCategoria.objects.filter(categoria=catslug)
    productos = Producto.objects.filter(categoria=catslug)
    paginator = Paginator(productos, 8)
    page = request.GET.get('page')
    paged_productos = paginator.get_page(page)
    categorias = Categoria.objects.all()
    producto_count = productos.count()
    context = {
        'tipo':tipo,
        'subCat':subcat,
        'categorias':categorias,
        'productos': paged_productos,
        'producto_count': producto_count,

    }
    return render(request, 'app/tienda/store.html', context)


# filtro de subcategoria
def subCatfilter (request,slugcat,subcatslug):
     # Trae todo
    categorias = Categoria.objects.all()

    #obtiene la subcategoria seleccionada
    subcatfilter =  SubCategoria.objects.get(slug=subcatslug) 

    # filtrar
    productos = Producto.objects.filter(subcategoria=subcatfilter) # filtra los producto por subcategoria
    
    # devuelve las subcategorias de la categoria seleccionada
    cat = Categoria.objects.get(slug =slugcat )
    subcat = SubCategoria.objects.filter(categoria=cat)

    # devuelve los tipos de intrumentos de la subcategoria
    tipo = TipoInstrumento.objects.filter(subcategoria= subcatfilter)
    producto_count = productos.count()
    

    context = {
        'tipo':tipo,
        'subCat':subcat,
        'categorias':categorias,
        'productos': productos,  
        'producto_count': producto_count,
    }
    return render(request, 'app/tienda/store.html', context)




def tipoisntruFilter (request,slugcat,subcatslug, tiposlug):
     # Trae todas las categorias
    categorias = Categoria.objects.all()

    #obtiene la subcategoria seleccionada
    subcatfilter =  SubCategoria.objects.get(slug=subcatslug) 
    tipoins =  TipoInstrumento.objects.get(slug=tiposlug) 

    # filtrar   
    cat = Categoria.objects.get(slug =slugcat )
    subcat = SubCategoria.objects.filter(categoria=cat)
    
    tipo = TipoInstrumento.objects.filter(subcategoria= subcatfilter)
    productos = Producto.objects.filter(subcategoria=subcatfilter ,tipoinstrumento= tipoins )
    producto_count = productos.count()
    

    context = {
        'tipo':tipo,
        'subCat':subcat,
        'categorias':categorias,
        'productos': productos,  
        'producto_count': producto_count,
    }
    return render(request, 'app/tienda/store.html', context)

def DetalleProducto(request, id):
    try:
        producto = Producto.objects.get(SKU=id)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request),producto=producto).exists()
    except Exception as e:
        raise e
    
    context={
        'producto': producto,
        'int_cart': in_cart
    }
    return render(request, 'app/tienda/detalle_producto.html',context)


# CRUD funciones

# Render crud  y trae todos los productos y categorias
def crud (request):
    producto  = Producto.objects.all()
    categoria  = Categoria.objects.all()
    subcat  = SubCategoria.objects.all()
    marca  = Marca.objects.all()
    tipoins  = TipoInstrumento.objects.all()
    contex = {'productos':producto,
              'categorias':categoria,
              'tipoi':tipoins,
              'marcas':marca,
              'subcat':subcat}
    return render(request,'Tcrud/crud.html',contex)

@permission_required('app.add_producto')
def agreProducto(request):
    datos = {'form': productoForm()}
    print(datos)
    if request.method == 'POST':
        formulario = productoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto agregado corectamente")
            return redirect('productosList')
        else:
            datos ["form"] = formulario
            
    return render(request, 'Tcrud/agreProducto.html', datos)

@permission_required('app.add_producto')
def agreCategoria (request): 
    datos = {'form': CategoriaForm()}
    if request.method == 'POST':
        formulario = CategoriaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Categoria agregada corectamente")
            return redirect('categoriasList')
    return render(request,'Tcrud/agreCategoria.html',datos)


def agreMarca (request): 
    datos = {'form': marcaForm()}
    if request.method == 'POST':
        formulario = marcaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Marca agregada correctamente")
            return redirect('MarcaList')
    return render(request,'Tcrud/agreMarca.html',datos)

@permission_required('app.add_producto')
def delete_marca(request, nombreMarca):
    marca = Marca.objects.get(nombreMarca=nombreMarca)
    marca.delete()
    messages.success(request, "Marca Borrada Correctamente")
    return redirect(to="MarcaList")


@permission_required('app.add_producto')
def agreTipoIns (request): 
    datos = {'form': tipoiForm()}
    if request.method == 'POST':
        formulario = tipoiForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Tipo Instrumento Agregado Correctamente")

            return redirect('tipoinsList')
    return render(request,'Tcrud/agreTipoIns.html',datos)


@permission_required('app.add_producto')
def agreSubcat (request): 
    datos = {'form': subCatForm()}
    if request.method == 'POST':
        formulario = subCatForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "SubCategoria Agregada Correctamente")
            return redirect('subcateList')
    return render(request,'Tcrud/agreSubcat.html',datos)


# CRUD funciones modificar
@permission_required('app.add_producto')
def Mod_Producto(request, SKU):
    producto = Producto.objects.get(SKU=SKU)
    datos = {
        'form': productoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = productoForm(data=request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Modificados correctamente"
            messages.success(request, "Modificado correctamente")
            return redirect('productosList')
    return render(request, 'Tcrud/modProducto.html', datos)

# CRUD funciones delete
@permission_required('app.add_producto')
def delete_Producto(request,SKU):
    producto = Producto.objects.get(SKU=SKU)
    producto.delete()
    return redirect(to="productosList")


def del_user(request, email):    
    try:
        u = User.objects.get(email = email)
        u.delete()
        messages.success(request, "The user is deleted")     
        return redirect ('vistaAdmin')       

    except User.DoesNotExist:
        messages.error(request, "User doesnot exist")    
        return redirect ('vistaAdmin')



def vistaAdmin(request):
    usuarios = User.objects.all()
    contex = {'usuarios':usuarios}
    return render (request,'app/admini/user_crud.html', contex)

# @login_required(login_url='login')

@permission_required('app.add_producto')
def cli_dashboard(request):
    return render(request,'app/cliente_dashboard.html')


@permission_required('app.add_producto')
def categoriasList(request):
    categoria  = Categoria.objects.all()
    contex = {
              'categorias':categoria
         }

    return render(request,"Tcrud/Listas/categorias.html",contex)

@permission_required('app.add_producto')
def delete_categoria(request,nombreCategoria):
    categoria = Categoria.objects.get(nombreCategoria=nombreCategoria)
    categoria.delete()
    return redirect(to="categoriasList")


@permission_required('app.add_producto')
def productosList(request):
    producto  = Producto.objects.all()
    contex = {
              'productos':producto
         }

    return render(request,"Tcrud/Listas/productos.html",contex)

@permission_required('app.add_producto')
def MarcaList(request):
    marca  = Marca.objects.all()
    contex = {
              'marcas':marca
         }

    return render(request,"Tcrud/Listas/marcas.html",contex)

@permission_required('app.add_producto')
def subcateList(request):
    subcat  = SubCategoria.objects.all()
    contex = {
              'subcat':subcat
         }

    return render(request,"Tcrud/Listas/subcategorias.html",contex)

@permission_required('app.add_producto')
def delete_subcategoria(request,id):
    subcategoria = SubCategoria.objects.get(nombreSubCategoria=id)
    subcategoria.delete()
    return redirect(to="subcateList")


@permission_required('app.add_producto')
def tipoinsList(request):
    tipo  = TipoInstrumento.objects.all()
    contex = {
              'tipo':tipo
         }
    return render(request,"Tcrud/Listas/tipoitem.html",contex)

@permission_required('app.add_producto')
def delete_tipoinstrumento(request,id):
    tipoinstrumento = TipoInstrumento.objects.get(nombreTipoInstrumento=id)
    tipoinstrumento.delete()
    return redirect(to="tipoinsList")

def vendedorView(request):
    ordenes = Order.objects.all()
    print(ordenes)
    contex = {
              'ordenes':ordenes
         }

    return render(request,"app/admini/vendedor/vendedor.html",contex)


def detalleOrder(request,order):

    items = OrderProduct.objects.filter(order=order)
    contex = {
              'items':items,
                'order':order
         }

    return render(request,"app/admini/vendedor/detalleorder.html",contex)


def viewPerfil(request):
    return render(request,'app/tienda/Perfil/perfil.html')


def viewUbis(request):
    current_user = request.user 
    ubicacion = UserUbicacion.objects.filter(user = current_user)
    context = { 
        'ubicaciones': ubicacion
    }
    print(ubicacion)
    return render(request,'app/tienda/Perfil/ubicaciones.html', context)


@login_required(login_url='loginCli')
def newUbi(request):
    if request.method == 'POST':
        formulario = ubicacionForm(request.POST)
        if formulario.is_valid():
            ubi = formulario.save(commit=False)   # crea el objeto pero NO lo guarda todavía
            ubi.user = request.user               # le asigna el user logueado
            ubi.save()                            # ahora sí, guarda con user incluido
            return redirect('viewUbis')
    else:
        formulario = ubicacionForm()
    return render(request, 'app/tienda/Perfil/nuevaUbi.html', {'form': formulario})

def deleteUbi(request,ubi):
    current_user = request.user
    ubi = UserUbicacion.objects.get(user=current_user,ubicacion=ubi)
    ubi.delete()
    return redirect(to="viewUbis")


def modUbi(request,ubi): 
    current_user = request.user
    ubicacion = UserUbicacion.objects.get(user=current_user,ubicacion=ubi)
    datos = {
        'form': ubicacionForm(instance=ubicacion)
    }
    if request.method == 'POST':
        formulario = ubicacionForm(data = request.POST,instance=ubicacion)
        if formulario.is_valid():
            formulario.save()
            return redirect('viewUbis')
           
    return render(request,'app/tienda/Perfil/modUbi.html',datos)



def viewOrders(request):
    current_user = request.user 
    ordenes = Order.objects.filter(user = current_user)
    context = { 
        'orders': ordenes
    }
   
    return render(request,'app/tienda/Perfil/ordenes.html', context)

def detalleUserOrder(request,order):
    orderOBJ = Order.objects.get(order_number=order)
    items = OrderProduct.objects.filter(order=order)
    contex = {
              'items':items,
                'order':order,
                'objOrder':orderOBJ,
         }

    return render(request,"app/tienda/Perfil/detalleUserOrder.html",contex)