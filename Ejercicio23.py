# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 00:42:25 2019

@author: Jesús García
"""
##Ejercicio: 23 "Área de un polígono regular "
##Un polígono es regular si sus lados tienen la misma longitud y los ángulos entre todos
##Los lados adyacentes son iguales. El área de un polígono regular se puede calcular usando
##la siguiente fórmula, donde s es la longitud de un lado   es el número de lados:
##área = n × s**2/4 × tan(π/n). Escriba un programa que lea s y n del usuario y 
##luego muestre el área de un polígono regular construido a partir de estos valores.

import math
pi=3.1416
s=int(input('Introduce la longitud: '))
n=int(input('Introduce el número de lados: '))

Area=(n*(s**2))/(4*(math.tan(pi/n)))

print('El area de un polígono regular es de: ',Area)