# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 14:36:54 2019

@author: Jesús García
"""

##Ejercicio 34: 'Segunda unidad'
##Escriba un programa que lea un número  entero introducido por el usuario.Su programa debe
##desplegar un mensaje indicando si su número entero es par o impar.

numero= float(input('Inserte un numero entero: '))

if(numero%2==0):
    print(str(numero)+' es par')

else:
    print(str(numero)+' es impar') 