from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, "BlogApp/home.html")


def servicios(request):
    return render(request,"BlogApp/servicios.html")

def tienda(request):
   return HttpResponse("Tienda")

def blog(request):
    return render(request, "BlogApp/blog.html")

def contacto(request):
    return render(request, "BlogApp/contacto.html")
