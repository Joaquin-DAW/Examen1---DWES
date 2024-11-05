from django.shortcuts import render
from django.db.models import Q
from .models import Voto, Cliente, Cuentabancaria

# Create your views here.

def index(request):
    return render(request, 'index.html') 

#1- El último voto que se realizó en un modelo principal en concreto, y mostrar el comentario, 
#la votación e información del usuario o cliente que lo realizó.
def ultimo_voto(request):
    votos = Voto.objects.select_related("herramienta", "cliente").order_by('-fecha_votacion')[:1].get()
    return render(request, "voto/ultimo_voto.html", {"votos": votos})

#2- Todos los modelos principales que tengan votos con una puntuación numérica menor a 3 y que realizó un usuario o cliente en concreto.
def voto_menor_tres(request, cliente):
    votos = Voto.objects.select_related("herramienta", "cliente").filter(cliente__nombre=cliente, puntuacion__lt=3).all()
    return render(request, "voto/voto_menor.html", {"votos": votos, "cliente":cliente})

#3- Todos los usuarios o clientes que no han votado nunca y mostrar información sobre estos usuarios y clientes al completo.
def clientes_sin_voto(request):
    clientes = Cliente.objects.prefetch_related("herramienta","cuenta_bancaria_cliente","votos_cliente").filter(votos_cliente__fecha_votacion=None).all()
    return render(request, "cliente/clientes_sin_voto.html", {"clientes": clientes})

#4- Obtener las cuentas bancarias que sean de la Caixa o de Unicaja y que el propietario tenga un nombre que contenga un texto en concreto, 
# por ejemplo “Juan”.
def cuentas_bancarias_banco(request, texto):
    cuentas = Cuentabancaria.objects.select_related("cliente").filter(Q(banco__icontains="CAIXA") | Q(banco__icontains="UNICAJA"), cliente__nombre=texto).all()
    return render(request, "cuenta/cuentas_bancarias_banco.html", {"cuentas": cuentas, "texto": texto})

#5- Obtener los votos de los usuarios que hayan votado a partir del 2023 con una puntuación numérica igual a 5  y que tengan asociada una cuenta bancaria.
def usuarios_votos_2023(request):
    clientes = Cliente.objects.prefetch_related("herramienta","cuenta_bancaria_cliente","votos_cliente").filter(votos_cliente__fecha_votacion__year__gt=2023, 
                                                                                                            votos_cliente__puntuacion=5,
                                                                                                            cuenta_bancaria_cliente__isnull=False).all() # Verifica que el que existe una cuenta bancaria al no tener un valor null
    return render(request, "cliente/clientes_con_votos_2023.html", {"clientes": clientes})

#6- Obtener todos los modelos principales que tengan una media de votaciones mayor del 2,5






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