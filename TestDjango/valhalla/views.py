from django.shortcuts import redirect, render
from . models import Proveedor
from . forms import ProveedorForm


def index(request):
    return render(request, 'index.html')
def tienda(request):
    return render(request, 'tienda.html')
def proveedor(request):
    proveedores = Proveedor.objects.all()
    return render(request,'proveedor.html', context={'datos':proveedores}
)

def form_proveedor(request):
    if request.method=='POST':
        form_proveedor = ProveedorForm(request.POST, files=request.FILES)
        if form_proveedor.is_valid():
            form_proveedor.save()
            return redirect('ver')
    else:
        form_proveedor = ProveedorForm()
    return render(request, 'valhalla/form_crearproveedor.html', {'form_proveedor':form_proveedor})

def ver(request):
    proveedores= Proveedor.objects.all()
    return render(request, 'valhalla/ver.html', {'proveedores': proveedores})

def form_modproveedor(request, id):
    proveedor=Proveedor.objects.get(idProv=id)
    datos ={
        'form': ProveedorForm(instance=proveedor)
    }
    if request.method == 'POST': 
        formulario = ProveedorForm(data=request.POST,files=request.FILES, instance = proveedor)
        if formulario.is_valid: 
            formulario.save()
            return redirect('ver')
    return render(request, 'valhalla/form_modproveedor.html', datos)

def form_delproveedor(request, id):
    proveedor = Proveedor.objects.get(idProv=id)
    proveedor.delete()
    return redirect('ver')





    

