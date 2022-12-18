from django.db import models

class Persona(models.Model):
    nombre_persona=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    fecha_nacimiento=models.DateField()
    dni=models.IntegerField()
    email=models.EmailField(max_length=50)

    def __str__(self):
        return f'({self.nombre_persona}, {self.apellido})'

class Producto(models.Model):
    codigo=models.CharField(max_length=10)
    fecha_elaboracion=models.DateField()
    precio=models.FloatField()
    nombre_producto=models.CharField(max_length=40)
    descripcion=models.CharField(max_length=100)
    def __str__(self):
        return f'({self.nombre_producto} y su precio es: {self.precio})'

class Proveedores(models.Model):
    numero_proveedor=models.IntegerField()
    razon_social=models.CharField(max_length=30)
    inicio_relacion=models.DateField()
    cuit=models.IntegerField()
    def __str__(self):
        return f'Provedos numero: {self.numero_proveedor} Razon social: {self.razon_social})'
