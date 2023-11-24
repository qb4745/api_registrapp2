from django.db import models


# Create your models here.
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=100)
    rol = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}  {self.correo}  {self.contrasena}  {self.rol}"


class Clase(models.Model):
    id = models.AutoField(primary_key=True)
    asignatura = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
    carrera = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.asignatura} {self.fecha}  {self.hora}  {self.carrera}"


class Clase_Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    id_clase = models.IntegerField()
    id_usuario = models.IntegerField()

    def __str__(self):
        return f"{self.id_clase} {self.id_usuario}"
