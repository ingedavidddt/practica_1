# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 22:37:15 2023

@author: david
"""
materias = ['ingles', 'vision', 'inteligencia', 'vision']
print(materias)
#al imprimir la lista se imprimen todo lo que la lista contenga
print(materias[1])
# podemos acceder solo un elemento de la lsiuta seleccionando el
# indice que queramos mostrar

mezcla = ['letras', 3434, 52.22]
# una lista puede contener todos los tipos de datos que soporta python
print(mezcla)
# imprimimos toda la lista
print(mezcla[1])
# imprimimos un elemento de la lista

numeros = ['cero', 'uno','dos', 'tres', 'cuatro', 'cinco']
print(numeros[-1])
print(numeros[-6])
# podemos invertir el orden de la lista al introducir posiciones 
# negativas lo cual hara que el ultimo elemento de la lista sea el 
# primero

del numeros[0]
# de esta manera podemos eliminar elemento de una lista
print(numeros)

del numeros[-1]
# al igual que para mostrar datos con posiciones negativas tambien se pueden
# eliminar elementos de esta manera
print(numeros)

numeros.remove('uno')
# con este metodo podemosmeliminar elementos especificos de una lista 
# especificando el valor que queremos eliminar
print(numeros)

numeros.pop()
# con este metodo podemos eliminar únicamente el último elemento de una lista
print(numeros)

elemento_eliminado = numeros.pop(0)
# con este metodo tembienpoemos eliminar elementos segun la posicion
# seleccionada con la ventaje de que podemos guardar el elemento eliminado
print("el elemento eliminadao de la lista es: ", elemento_eliminado)

numeros.append('cinco')
# con este metodo podemos añadir elementos al final de la lista
print(numeros)

numeros.insert(0,'cero')
# con este metodo podemos insertar elementos en la posicion que deseemos
# de la lista
print(numeros)

numeros = ['cero', 'uno','dos', 'tres', 'cuatro', 'cinco']
numeros.sort()
# con este metodo podemos ordenar los elementos en orden alfabetico ascendente
# pero afecta permanentemente el orden de la lista
print(numeros)

numeros.sort(reverse=True)
# de esta manera podemos ordenar los elementos en orden descendente
print(numeros)

numeros = ['cero', 'uno','dos', 'tres', 'cuatro', 'cinco']
print(sorted(numeros))
# de esta manera solo se alterara el orden de manera temporal al momento de 
# imprimir el valor pero el orden la la lista permanecera intacto despues de esto
print(numeros)


n_numeros = len(numeros)
# de esta manera podemos conocer la cantidad de elementos que conforman una lista
print(n_numeros)