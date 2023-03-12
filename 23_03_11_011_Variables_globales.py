# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 23:21:02 2023

@author: david
"""

def cuenta1():
# para utilizar variables que estén dentro de una función desde fuera esnecesario declararlas como globales
    global x
    
    for x in range (0, 5):
        x += 1
        print(x, "\n")
        
# para anidar una funcion dentro de otra basta con declarla dentro de la que deseemos
# y despues llamarla dentro de la funcion anterior para poder ser utilizada        
    def imprime():
        print(x)
        
    imprime()
            
cuenta1()

# la variable x comenzara a contar desde 5 ya que en la funcion anterior su ultimo valor
# fue de 5 y al final de esta funcion sera de 10
for y in range (0, 5):
    x += 1

print(x)