# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 22:14:20 2023

@author: david
"""

class registro:
# dentro de la clase se pueden tener la cantidad de atributos que se deseen
    usuario = ''
    hora_entrada= ''
    
    def mostrar(self):
        # la palabra reservada self sirve para referirce a si mismo
        print('usuario: ', self.usuario, '\nhora de entrada: ', self.hora_entrada)
        
usuario1 = registro()
# creamos un objeto llamado "usuario1" que pertenece a la clase registro

usuario1.usuario = 'alfalfas' 
usuario1.hora_entrada = '12.20'
# de esta manera se le asignan o cambian los valores a los atributos del usuario 

usuario1.mostrar()
# finalmente mostramos los datos del usuario

# super clase
class alumno:
    
    def __init__(self, nombre, promedio, edad):
        #EL USO DE__init__ establece que deberan de especificarce los valores de
        #nombre y promedio en este caso al momento de crear un objeto de esta clase
        self.nombre = nombre
        self.promedio = promedio
        self.edad = edad
        
    def mostrar(self):
        print('Nombre:', self.nombre, '\npromedio:', self.promedio, '\nedad:', self.edad)
        
alumno1 = alumno("shiraori", "100", "20")
alumno1.mostrar()



# para poder utilizar los atributos de otra clase creada recurrimos a la herencia
# la cual nos permite utilizar atributos de otras clases y añadir los propios
# creando una subclase de alumno en este caso
class topAlumnos(alumno):
    logro = ''
    
    def mostrarSA(self):
        print('Nombre:', self.nombre, '\nedad:', self.edad, '\npromedio:', 
              self.promedio, '\nlogro:', self.logro)
        
sAlumno1 = topAlumnos("kaori", "100", "21")
sAlumno1.logro = "gano el duelo a muerte con cucchillos"
sAlumno1.mostrarSA()
    
del alumno1.edad
# podemos eliminar atributos de un objeto de esta manera o el objeto solo 
# especificando el nombre de este

class bottomAlumnos(alumno):
    def __init__(self, nombre, promedio, edad, motivo):
        self.nombre = nombre
        self.promedio = promedio
        self.edad = edad
        self.motivo = motivo
        
    def mostrarSA(self):
        print('Nombre:', self.nombre, '\nedad:', self.edad, '\npromedio:', 
              self.promedio, '\nedad:', self.edad, '\nmotivo del bajo desempeño:', self.motivo)
        
bAlumno1 = bottomAlumnos("miku", "45", "22", "no puede asistir a clases todos los dias")
#si en las subclases redeclaras cosas, prevalecen las redeclaraciones pertenecientes a la propia clase.

bAlumno1.mostrarSA()