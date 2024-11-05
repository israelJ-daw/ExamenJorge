from django.shortcuts import render
from .models import *
from django.http import HttpResponseForbidden, HttpResponseNotFound, HttpResponseServerError, HttpResponseBadRequest

# Create your views here.


def index(request):
    return render(request, "index.html")

def ultimo_voto(request, vendido_id):
    ultimos=Puntuacion_cuadernos.objects.prefetch_related("vendido", "usuario").all()
    #hago un first porque lo ordeno por fecha de puntucion y esta ordenado de tal manera que el primero que se coge es el mas reciente y por eso hago un first para coger el primero 
    ultimos= ultimos.filter(vendido_id=vendido_id).order_by("fecha_puntuacion").first()
    return render(request, "ultimo_voto.html", {"ultimos" : ultimos}) 


    

#Vista errores
def error_404(request, exception=None):
    return render(request, 'errores/error_404.html',None, None,404)

def error_500(request, exception=None):
    return render(request, 'errores/error_500.html', None, None,500)

def error_403(request, exception=None):
    return render(request, 'errores/error_403.html',None , None,403)

def error_400(request, exception=None):
    return render(request, 'errores/error_400.html',None,None,400)