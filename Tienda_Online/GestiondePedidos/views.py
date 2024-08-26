from django.shortcuts import render
from django.http import HttpResponse

def busqueda(request):
    
    return render(request, 'Busqueda.html')

def buscar(request):

    mensaje = "Articulo Buscado: %r" %request.GET["prd"]

    return HttpResponse(mensaje)