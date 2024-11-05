from django.db import models

# Create your models here.

class Herramienta(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Herramienta")
    precio = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)                                                                                                                                                                          
    descripcion = models.TextField(blank=True)
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo_electronico = models.EmailField(unique=True)
    edad = models.IntegerField(null=True)
    herramienta = models.ManyToManyField(Herramienta, related_name="cliente_herramienta")

class Cuentabancaria(models.Model):
    numero_cuenta = models.CharField(max_length=20, unique=True)
    banco = models.CharField(max_length=50, choices=[
        ('CAIXA', 'Caixa'),
        ('BBVA', 'BBVA'),
        ('UNICAJA', 'Unicaja'),
        ('ING', 'ING')], blank=True)
    descripcion = models.TextField(blank=True)
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE, related_name="cuenta_bancaria_cliente")
    
    
class Voto(models.Model):
    puntuacion = models.IntegerField()
    comentario = models.TextField(blank=True)
    fecha_votacion = models.DateTimeField(auto_now_add=True)
    herramienta = models.ForeignKey(Herramienta, on_delete=models.CASCADE, related_name="votos_herramienta")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="votos_cliente")
