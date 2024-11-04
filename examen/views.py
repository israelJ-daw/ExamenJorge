from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "index.html")



#Vista errores
def error_404(request, exception=None):
    return render(request, 'errores/error_404.html',None, None,404)

def error_500(request, exception=None):
    return render(request, 'errores/error_500.html', None, None,500)

def error_403(request, exception=None):
    return render(request, 'errores/error_403.html',None , None,403)

def error_400(request, exception=None):
    return render(request, 'errores/error_400.html',None,None,400)