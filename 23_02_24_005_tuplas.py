# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 23:05:34 2023

@author: david
"""

tupla = ('rojo', 'azul', 'verde', 'amarillo')
# las tuplas son como las listas pero estas se escriben con parentesis
# ademas de que estas no pueden ser modificadas y al igual que ñlas listas
# soportan y todos los tipos de datos
print(tupla[0])
# al igual que con las listas podemos acceder a cualquier elemento de la lista

lista = list(tupla)
# de esta manera podemos convertir una tupla a una lista
print(lista)
print(type(lista))
# de esta forma podemos saber el tipo de dato

lista = [1, 2 , 3,'lista']
tupla = tuple(lista)
print(tupla)
# de esta forma podemos convertir una lsita en una tupla
print(type(tupla))
