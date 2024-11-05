from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html') 



#Aquí creamos las vistas para cada una de las cuatro páginas de errores que vamos a controlar.

#Este error indica que el servidor no entiende la solicitud del navegador.
def error_400(request,exception=None):
    return render(request, 'errores/400.html',None,None,400)

#Este error indica que el usuario no tiene permisos para acceder a la página.
def error_403(request,exception=None):
    return render(request, 'errores/403.html',None,None,403)

#Este error se produce cuando el servidor no puede encontrar la página solicitada.
def error_404(request,exception=None):
    return render(request, 'errores/404.html',None,None,404)

#Este error ocurre cuando hay un proble interno en el servidor.
def error_500(request,exception=None):
    return render(request, 'errores/500.html',None,None,500)