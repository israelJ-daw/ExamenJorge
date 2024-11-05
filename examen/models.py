from django.db import models
from django.utils import timezone

#Tengo los modelos de alquiler, tienen 10 parametros distintos y 10 campos distintos

class Cuaderno(models.Model):
    color=models.CharField(max_length=100, verbose_name="Color del cuaderno")
    tipo=models.EmailField(max_length=254, db_column="Tipo_cuaderno")
    diamametro = models.CharField(max_length=20, blank=True)
    Precio = models.FloatField()
    


class Usuario(models.Model):
    nombre=models.CharField(max_length=100, verbose_name="Nombre del Usuario")
    cuenta=models.TextField(max_length=10, verbose_name="Cuenta Bancaria")
    num_cuenta=models.TextField(unique=True)
    fecha_registro = models.DateTimeField(db_column="fecha", default=timezone.now)
    
    usuarios=models.ManyToManyField(Cuaderno,related_name="Usuarios_cuadernos")
    

class Vendidos(models.Model):
    
    color=models.CharField(max_length=100)
    tipo=models.EmailField(max_length=254)
    diamametro = models.CharField(max_length=20, blank=True)
    Precio = models.FloatField()
    
    vendidos = models.ForeignKey(Cuaderno, on_delete=models.CASCADE, related_name="Vendidos")
        
class Puntuacion_cuadernos(models.Model):
    descripcion=models.TextField( )    
    fecha_puntuacion = models.DateTimeField(default=timezone.now)
    puntuacion = models.IntegerField()
        
    vendido = models.ForeignKey(Vendidos, on_delete=models.CASCADE, related_name="Cuadernos_vendidos", null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="Usuarios_puntuados", null=True)
    
    
class Subscripcion(models.Model):
    precio = models.IntegerField()
    BANCO=[
        ("BBVA", "Banco Bilbao Vizcaya Argentaria"),
        ("Caixa", "CaixaBank"),
        ("UNICAJA", "Unicaja Banco"),
        ("ING", "ING BANK NV,"),]
    
    usuarios=models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="Usuarios_Subscripto", null=True)
