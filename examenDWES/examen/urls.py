from django.urls import path
from .import views

urlpatterns = [
    
    path('',views.index,name='index'),
    
    path('ultimo_voto',views.ultimo_voto, name='ultimo_voto'),
    path('voto_menor/<str:cliente>/',views.voto_menor_tres, name='voto_menor_tres'),
    path('clientes_sin_voto',views.clientes_sin_voto, name='clientes_sin_voto'),
    path('cuentas_bancarias_banco/<str:texto>/',views.cuentas_bancarias_banco, name='cuentas_bancarias_banco'),
    path('usuarios_votos_2023',views.usuarios_votos_2023, name='usuarios_votos_2023'),
    path('media_concreta',views.media_concreta, name='media_concreta'),
]