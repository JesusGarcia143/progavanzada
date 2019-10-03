# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 00:30:41 2019

@author: Jesús García
"""
##Ejercicio: 21 "Área de un triángulo"
#El área de un triángulo se puede calcular usando la siguiente fórmula, donde b es la 
##longitud de la base del triángulo, y h es su altura: área =(b × h)/2
#Escriba un programa que permita al usuario ingresar valores para b y h. 
#El programa luego debe calcular y mostrar el área de un triángulo con longitud base b y
##altura h.

h=int(input('Introduce la altura del triangulo: '))
b=int(input('Introduce la base del triangulo: '))

area=(b*h)/2

print('El area de un triangulo es de: ',area)
