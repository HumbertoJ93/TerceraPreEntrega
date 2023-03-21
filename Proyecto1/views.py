from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def PrimeraVista(request):
    return HttpResponse('Primera vista')

def registro(request):
    return render(request, "registro.html")