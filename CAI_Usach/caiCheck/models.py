from django.db import models

# Create your models here.
class Usuario(models.Model):
    rut = models.CharField(max_length=12, primary_key=True)
    correo = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=50)


class Rol(models.Model):
    id = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=50)


class Participante(models.Model):
    id = models.IntegerField(primary_key=True)
    rut = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    telefono1 = models.CharField(max_length=12)
    telefono2 = models.CharField(max_length=12)
    correo1 = models.CharField(max_length=50)
    correo2 = models.CharField(max_length=50)


class Curso(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    ciclo = models.CharField(max_length=50)
    año = models.IntegerField()
    malla = models.CharField(max_length=50)
    inicio = models.DateField()
    termino = models.DateField()
    duracion = models.IntegerField()
    codigo_sence = models.CharField(max_length=50)
    asistencia_minima = models.IntegerField()
    calificacion_minima = models.IntegerField()
    modalidad = models.CharField(max_length=50)


class Empresa(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    rut = models.CharField(max_length=12)


class Contacto(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    rut = models.CharField(max_length=12)
    correo = models.CharField(max_length=50)


######### Tablas intermedias #########

class Usuario_Rol(models.Model):
    id = models.IntegerField(primary_key=True)
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    rut = models.ForeignKey(Usuario, on_delete=models.CASCADE)


class Participante_Curso(models.Model):
    id = models.IntegerField(primary_key=True)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    id_participante = models.ForeignKey(Participante, on_delete=models.CASCADE)
    calificacion = models.IntegerField()
    asistencia = models.IntegerField()
    condicion = models.CharField(max_length=10)


class Participante_Empresa(models.Model):
    id = models.IntegerField(primary_key=True)
    id_participante = models.ForeignKey(Participante, on_delete=models.CASCADE)
    id_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
