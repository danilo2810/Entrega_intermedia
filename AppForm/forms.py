from django import forms

class PersonaForm(forms.Form):
    nombre_persona=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    fecha_nacimiento=forms.DateField()
    dni=forms.IntegerField()
    email=forms.EmailField(max_length=50)

class ProductoForm(forms.Form):
    codigo=forms.CharField(max_length=10)
    fecha_elaboracion=forms.DateField()
    precio=forms.FloatField()
    nombre_producto=forms.CharField(max_length=40)
    descripcion=forms.CharField(max_length=100)

class ProveedoresForm(forms.Form):
    numero_proveedor=forms.IntegerField()
    razon_social=forms.CharField(max_length=30)
    inicio_relacion=forms.DateField()
    cuit=forms.IntegerField()

