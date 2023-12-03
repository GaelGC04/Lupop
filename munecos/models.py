from django.db import models
from django.contrib.auth.models import User


class Tamano(models.Model):
    altura = models.FloatField()
    # altura del muneco
    anchura = models.FloatField()
    # anchura del muneco

    def __str__(self):
        return f"{self.id} - {self.altura} - {self.anchura}"


class Categoria(models.Model):
    tipo = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.id} - {self.tipo}"


class Muneco(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    categoria = models.ManyToManyField(Categoria)
    # un muneco puede tener varias categorias
    # por ejemplo: Superman tiene las categorías accion, peliculas y DC comics

    precio = models.FloatField()
    tamano = models.ForeignKey(Tamano, on_delete=models.CASCADE)
    descripcion = models.TextField()
    estrellas = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    # se muestra media de las estrellas dadas por usuarios

    def __str__(self):
        return f"{self.id} - {self.nombre}"


class Opinion(models.Model):
    muneco = models.ForeignKey(Muneco, on_delete=models.CASCADE, related_name='opiniones')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()
    estrellas = models.PositiveIntegerField(default=0, blank=True)

    def __str__(self):
        return f"{self.id} - {self.usuario.username} - {self.muneco.nombre}"