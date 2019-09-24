# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 14:30:50 2019

@author: Jesús García
"""
#Ejercicio 7: Escriba un programa que lea un número positivo n, insertado por el usuario y despues 
#despliegue la suma de todos los enteros desde 1 hasta n. La suma de los primeros 
#enteros n positivos puede ser calculado usando la formula
#suma= (n)(n+1)/2

n= int(input('Inserte un numero positivo: '))
suma= int(((n *(n +1 ))/ 2 ))
print('La suma de todos los numeros positivos es: ' , suma)

