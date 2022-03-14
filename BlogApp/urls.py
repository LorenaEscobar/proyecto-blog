from django.urls import path

from BlogApp import views

urlpatterns = [
    path('', views.home, name="Inicio"),
    path('', views.servicios, name="Servicios"),
    path('', views.tienda, name="Tienda"),
    path('', views.blog, name="Blog"),
    path('', views.contacto, name="Contacto"),
]