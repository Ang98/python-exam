from django.shortcuts import render
from .models import Usuario
# Create your views here.

def Principal(request):

    return render(request,'index.html')

def Nosotros(request):

    return render(request,'nosotros.html')

def Servicios(request):

    return render(request,'servicios.html')