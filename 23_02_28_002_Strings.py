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

nombre_completo = nombre + ' ' + apellido
# tambien se le pueden agragar espacios extras utilizando comillas
print(nombre_completo)


n1 = '2'
n2 = '5'
# para concatenar numeros, estos tienen que ser declarados como strings ya que
# si se declaran sin estas sera una suma normal entre dos numeros
print(n1 + n2)


nombre_completo = nombre_completo.title()
# con el metodo title se transforma la primer letra de cada palabra en mayuscula
print(nombre_completo)

nombre = "david".title()
# el metodo title tambien puede ser utilizado de esta forma o directamente
# desde la funcion print
print(nombre)

print(nombre_completo.upper())
# el metodo upper() convierte todos los caracteres en mayusculas

lower = "ESTO ES LO QUE HACE EL METODO LOWER"

print(lower.lower())
#el metodo lower() transforma todo en minusculas


v1 = "materias:"
v2 = "inteligencia artificial"
v3 = "vision artificial"
v4 = "PLC"

print(v1 + "\n",v2 + "\n",v3 + "\n",v4)
#para utilizar un salto de linea entre cada impresion se utilizando \n cada 
#vez que querramos usar un salto de linea

print(v1 + "\t",v2 + "\t",v3 + "\t",v4)
#para hacer tabulaciones se utiliza "\t" cada vez que se quiera realizar una
#tabulacion