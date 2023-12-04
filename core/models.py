from django.db import models

class Seccion1(models.Model):
    OPCIONES_COLORES = [
        ('rojo-pastel', 'rojo-pastel'),
        ('azul-pastel', 'azul-pastel'),
        ('verde-pastel', 'verde-pastel'),
        ('amarillo-pastel', 'amarillo-pastel'),
        ('naranja-pastel', 'naranja-pastel'),
        ('negro', 'negro'),
        ('grafito', 'grafito'),
        ('blanco', 'blanco'),
    ]
    titulo = models.CharField(max_length=255, unique=True)
    descripcion = models.TextField()
    color_fondo = models.CharField(max_length=20, choices=OPCIONES_COLORES)
    imagen_fondo = models.ImageField(upload_to='seccion1/', null=True, blank=True)
    enlace_url = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{self.id} - {self.titulo}'


class Seccion2(models.Model):
    OPCIONES_COLORES = [
        ('rojo-pastel', 'rojo-pastel'),
        ('azul-pastel', 'azul-pastel'),
        ('verde-pastel', 'verde-pastel'),
        ('amarillo-pastel', 'amarillo-pastel'),
        ('naranja-pastel', 'naranja-pastel'),
        ('negro', 'negro'),
        ('grafito', 'grafito'),
        ('blanco', 'blanco'),
    ]
    titulo = models.CharField(max_length=255, unique=True)
    descripcion = models.TextField()
    color_fondo = models.CharField(max_length=20, choices=OPCIONES_COLORES)
    imagen_fondo = models.ImageField(upload_to='seccion2/', null=True, blank=True)
    enlace_url = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{self.id} - {self.titulo}'


class Seccion3(models.Model):
    OPCIONES_COLORES = [
        ('rojo-pastel', 'rojo-pastel'),
        ('azul-pastel', 'azul-pastel'),
        ('verde-pastel', 'verde-pastel'),
        ('amarillo-pastel', 'amarillo-pastel'),
        ('naranja-pastel', 'naranja-pastel'),
        ('negro', 'negro'),
        ('grafito', 'grafito'),
        ('blanco', 'blanco'),
    ]
    titulo = models.CharField(max_length=255, unique=True)
    descripcion = models.TextField()
    color_fondo = models.CharField(max_length=20, choices=OPCIONES_COLORES)
    imagen_fondo = models.ImageField(upload_to='seccion3/', null=True, blank=True)
    enlace_url = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{self.id} - {self.titulo}'

