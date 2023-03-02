# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 08:30:40 2023

@author: david
"""

x = 0
c = 0

print("ciclo while\n\n")

while x != 4 :
# la funcion while crea un bucle infinito que se rompera hasta que s ecumplan 
# las condiciones establecidas    
   
  
    x  = int(input("adivina un numero entre 0 y 5\n"))
    
    if x > 5:
        print("el numero introducido es mayor que 5")
        continue
        # esta funcion hace que se regrese al comienzo del ciclo
    
    c += 1
    
    if x!= 4:
        
        if c > 3:
            print("fueron muchos intentos, adios")
            break
            # el operador break hace que salgamos del bucle
        print("vuelve a intentralo") 
    
    if x == 4:
        print("bien hecho")
        
print("\n\nciclo for\n\n")
    
numeros = ['cero', 'uno','dos', 'tres', 'cuatro', 'cinco']  

for x in numeros:
    print(x)
# con este ciclo lo que hacemos es que iteramos la lista numeros y 
# sus valores en x para despues imprimirlos

for x in numeros[0]:
    if x == 'r':
        continue
    print(x)   
# en este ciclo lo que se hace es iterar la palabra almacenada enla posicion 0
# para depues imprimir letra por letra esta variable.
# al igual que con el ciclo while se puede utilizar la funcion continue o break

for x in '':
	pass
# la funcion pass sirve para dejar un ciclo vacio como para cuando no sabemos
# que hacer con este ciclo, ademas tambien funciona con el cliclo while

print("\n\nciclo for cuando el tipo de dato es range()\n\n")

for x in range(5):
	print(x)
# con la funcion range() lo que hacemos es que el for recorra el valor de 0
# hasta 4 y a la vez lo imprima

for x in range(5,10):
	print(x)    
# con la funcion range() lo que hacemos es que el for recorra el valor de 5
# hasta 10 y a la vez lo imprima

for x in range(100, -100, -20):
	print(x)
# en este caso establecemos un rango de 100 a -100 y le damos el parametro para
# especificar en este caso el decremento de -20