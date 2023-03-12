# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 17:48:37 2023

@author: david
"""

datos = {
    'escuela' : 'ceti colomos',
    'grado' : 'quinto',
    'grupo' : 'E',
    'nombre' : 'david'
    
}
# de esta forma se puede crear un diciconario, el cual es capaz de guardar una 
# coleccion de objetos
consulta = datos['grado']

print(consulta)
# de esta forma se puede consultar un valor del diccionario con su clave

print(datos)
# de este modo se mostrara todo el diccionario

datos['nombre'] = 'david diaz'
# podemos modificar los valores del diccionario de este modo, ingresando la clave
# y despues el nuevo valor para esa clave

for x in datos:
    print(x)
    
# de esta forma podemos mostrar todas las claves que tiene un diccionario

for x in datos:
    print(datos[x])
    
# de esra forma podemos mostrar todos los valores alacenados en el diccionario

print("\n", len(datos), "\n")
# de esta manera podemos conocer el tamaño del diccionario

del(datos['grado'])
del(datos['grupo'])
# con el metodo del podemos elimiar todo el diccionario o solo una clave del mismo
print("\nnuevo tamaño despues de eliminar dos claves", len(datos), "\n")

datos['grado y grupo'] = "6E"
# asi podemos agragar nuevo elemntos al diccionario
print(datos)
