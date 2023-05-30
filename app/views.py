from django.shortcuts import  render, redirect
from carts.models import CartItem ,Cart
from carts.views import _cart_id, checkout, checkout2
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import User
from . models import *
from .models import SubCategoria, Categoria
from django.core.paginator import EmptyPage, PageNotAnInteger,Paginator

# Create your views here.

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
                User.objects.create_bodeguero(email,username,apellido,telefono,password) 
            elif tipo == 'vendedor':
                 User.objects.create_vendedor(email,username,apellido,telefono,password) 
            elif tipo == 'contador':
                User.objects.create_contador(email,username,apellido,telefono,password) 
            else:
                pass
            messages.success(request, 'te has registrado correctamente')
            return redirect(to='home')
        
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
                password = formulario.cleaned_data["password"]
                User.objects.create_user(email,username,password) 
                return redirect(to='home')
            data["form"] = formulario
    return render(request, 'registration/registroCli.html',data)


def asdasdas (request):
    
    if request.method == 'GET':
       data = { 'form' : Ordenform()}
       return render(request, 'registration/registroCli.html',data)
    
    else:
        if request.method == 'POST':
            formulario = Ordenform(data= request.POST)
            if formulario.is_valid():
                email = formulario.cleaned_data["email"]
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
    subcat = SubCategoria.objects.filter(slugcat=slugcat)
    productos = Producto.objects.filter(subcategoria=subcatfilter)
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




def tipoisntruFilter (request,slugcat,subcatslug):
     # Trae todo
    categorias = Categoria.objects.all()

    #obtiene la subcategoria seleccionada
    subcatfilter =  SubCategoria.objects.get(slug=subcatslug) 

    # filtrar
    subcat = SubCategoria.objects.filter(slugcat=slugcat)
    productos = Producto.objects.filter(subcategoria=subcatfilter)
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

# Agrega un nuevo producto
def agreProducto(request):
    datos = {'form': productoForm()}
    print(datos)
    if request.method == 'POST':
        formulario = productoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Datos guardados correctamente"
            return redirect('crud')
        else:
            datos ["form"] = formulario
            
    return render(request, 'Tcrud/agreProducto.html', datos)


def agreCategoria (request): 
    datos = {'form': CategoriaForm()}
    if request.method == 'POST':
        formulario = CategoriaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Datos guardados correctamente"
            return redirect('crud')
    return render(request,'Tcrud/agreCategoria.html',datos)

def agreMarca (request): 
    datos = {'form': marcaForm()}
    if request.method == 'POST':
        formulario = marcaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Datos guardados correctamente"
            return redirect('crud')
    return render(request,'Tcrud/agreMarca.html',datos)

def agreTipoIns (request): 
    datos = {'form': tipoiForm()}
    if request.method == 'POST':
        formulario = tipoiForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Datos guardados correctamente"
            return redirect('crud')
    return render(request,'Tcrud/agreTipoIns.html',datos)

def agreSubcat (request): 
    datos = {'form': subCatForm()}
    if request.method == 'POST':
        formulario = subCatForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Datos guardados correctamente"
            return redirect('crud')
    return render(request,'Tcrud/agreSubcat.html',datos)


# CRUD funciones modificar

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
            return redirect('crud')
    return render(request, 'Tcrud/modProducto.html', datos)

# CRUD funciones delete

def delete_Producto(request,SKU):
    producto = Producto.objects.get(SKU=SKU)
    producto.delete()
    return redirect(to="crud")


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
    return render (request,'app/admini/Admincrud.html', contex)





def ver(request):
    user = request.user
    dueño = Cart.objects.get(user=user)
    item = CartItem.objects.filter(cart=dueño)

    for valor in item.values():
        print(valor)
    orden = Orden('default','ae@a.com','2323','valparaiso',222,'redcompra',232323)
    orden.save()


    #datos = Cart.objects.get()


    return redirect('crud')


