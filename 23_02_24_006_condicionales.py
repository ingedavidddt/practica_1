# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 23:35:33 2023

@author: david
"""

n1 = 20
n2 = 30
t = True
if n1 < n2:
    print("el primer numero es menor al segundo")
    
print("el valor de t es verdadero")    
if t == True:
    print("es verdad")
    t = False

print("¿y ahora?")    

if t == True:
    print("es verdad")
else:
    print("es falso")


dato = int(input("¿cuantos mangas has leido?\n"))
# con la funcion input() le permite al usuario ingresar datos

if dato <= 3:
    print("me decepcionas")
elif dato > 3 and dato <10:
    print("te hace falta odio")
elif dato > 10 and dato <20:
    print("vas por buen camino")
elif dato > 20:
    print("bien hecho")
    
# el condicional elif nos permite añadir multiples condicionales a los bloques if
# el operador and hace que se tengan que cumplir las dos condiciones a la vez

materias = ['teoria de control', 'ingles', 'economia', 'vision artificial']
entrada = input("introduce una materia que curses para saber si pertenece a sexto semestre\n")

if entrada in materias:
# con el operador "in" queremos saber si el dato que introduciomos en la entrada
# se encuentra dentro de la lista, y de ser asi el resultado sera verdadero
    print("tus materias pertenecen al sexto semestre")
    
else:
    print("tus materias no pertenecen a sextos emestre")
    
print("si es una materia de sexto") if 'economia' in materias else print("no es una materia de sexto")

