from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def registro(request):
    return render(request, "registro.html")

def contacto(request):
    return render(request, "contacto.html")

