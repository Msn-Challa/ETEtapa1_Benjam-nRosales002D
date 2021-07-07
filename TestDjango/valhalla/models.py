from django.db import models

# Create your models here.

class Categoria(models.Model):
    idCategoria=models.IntegerField(primary_key=True, verbose_name='Id de Categoria')
    nombreCategoria=models.CharField(max_length=60, verbose_name='Nombre de categoria')

    def __str__(self):
        return(self.nombreCategoria)

class Proveedor(models.Model):
    idProv=models.CharField(max_length=10, primary_key=True, verbose_name='Número de identificación')
    img=models.ImageField(null=True, verbose_name='Logo de proveedor')
    nombreP=models.CharField(max_length=50, verbose_name='Nombre de proveedor')
    numTf=models.IntegerField(verbose_name='Número de teléfono')
    dire=models.CharField(max_length=60, verbose_name='Dirección')
    email=models.CharField(max_length=50, verbose_name='Email')
    pais=models.CharField(max_length=60, verbose_name='País')
    moneda=models.CharField(max_length=7, verbose_name='Moneda de pago (Pesos o dólares)')
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return(self.idProv)
