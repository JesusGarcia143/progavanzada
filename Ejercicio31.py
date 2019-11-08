# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 00:31:23 2019

@author: Jesús García
"""
##Ejercicio: 31 "Suma de los dígitos en un entero"
##Desarrolle un programa que lea un número entero de cuatro dígitos del usuario y muestre 
##la suma de los dígitos en el número. Por ejemplo, si el usuario ingresa 3141, 
##entonces su programa debería mostrar 3 + 1 + 4 + 1 = 9.

numero=input('Introducir un numero entero de 4 digitos: ' )

a =int (numero [ 0 ])
a+=int (numero [ 1 ])
a+=int (numero [ 2 ])
a+=int (numero [ 3 ])

print (numero [ 0 ], ' + ' , numero [ 1 ], ' + ' , numero [ 2 ], ' + ' , numero [ 3 ], ' = ' , a)