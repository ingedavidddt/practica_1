# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 18:15:04 2023

@author: david
"""

def mul(d1, d2):
    print("el resultado de la multiplicacion es: ", d1 * d2)
# asi es como se crea una funcion, en este caso la funcion recibe
# dos argumentos de entrada
mul(4, 7)
# de este modo podemos llamar a la funcio creada anteriormente enviando
# los dos datos o argumentos requeridos para poder llamarla
    

def imprime(*a):
    print(a)
    print('el primer dato es: ' , a[0])
# con lso argumentos arbitrarios (*) + el numbre que le quieras dar podemos  
# ingresar un numero indeterminado de argumentos en las funciones
imprime(1, 2, 3, 4)





def cuenta(**m):
    print("el primer numero es es" + m["uno"] + "el ultimno numero es es" + m["dos"])
# para poder utilizar los diccionarios necesitamos usar (**) + el nombre que 
# le quieras dar, ya que estos tienen dos apartados
    
cuenta(uno = "primero", dos = "segundo")