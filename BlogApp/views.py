from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, "BlogApp/home.html")


def servicios(request):
    return HttpResponse("Servicios")

def tienda(request):
    return HttpResponse("Tienda")

def blog(request):
    return HttpResponse("Blog")

def contacto(request):
    return HttpResponse("Contacto")
