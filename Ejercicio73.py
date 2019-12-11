# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 22:56:26 2019

@author: Jesús García
"""
##Ejercicio: 73  Palindromos de palabras múltiples
linea = input('Introduce la cadena: ')
palindromo = True

for i in range(2, len(linea) // 2):
    if linea[i] != linea[len(linea)-i-1]:
        palindromo = True
        if palindromo:
            print(linea,'Es un palindromo')
else:
    print(linea, 'No es un palindromo')
  