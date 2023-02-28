# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 12:27:38 2023

@author: david
"""

mensaje = "esta es una tarea de 'IA'"
# se utilizan las comillas simples para poder resaltar un texto dentro de un string
# declarado con comillas dobles
print(mensaje)


mensaje = 'esta es otra forma de escribir que "la tarea es de IA"'
# utilizamos las comillas simples para declarar el string y resaltar el
# texto con comillas dobles
print(mensaje)

nombre = "david"
apellido = "diaz"

nombre_completo = nombre + apellido 
# se utiliza el operador de la suma para concatenar 2 strings

print(nombre_completo)

print(nombre + ' ' + apellido)
# tambien se le pueden agragar espacios extras utilizando comillas

n1 = '2'
n2 = '5'
# para concatenar numeros, estos tienen que ser declarados como strings ya que
# si se declaran sin estas sera una suma normal entre dos numeros
print(n1 + n2)

