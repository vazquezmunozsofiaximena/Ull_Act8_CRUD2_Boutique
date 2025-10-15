from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    puesto = models.CharField(max_length=50)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return f'Empleado: {self.nombre} {self.apellido} {self.puesto}'