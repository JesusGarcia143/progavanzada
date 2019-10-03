# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 23:46:37 2019

@author: Jesús García
"""
##Ejercicio: 16 "Area y Volumen"
##Escriba un programa que comience leyendo un radio, r, del usuario. El programa
##continúe calculando y mostrando el área de un círculo con radio r y el volumen de una
##esfera con radio r. Use la constante pi en el módulo matemático en sus cálculos.

##Sugerencia: El área de un círculo se calcula utilizando el área de fórmula = πr 2.
##El volumen de una esfera se calcula utilizando la fórmula volumen = 4/3πr^3.

import math
radio=int(input('ingrese el radio: '))

area=math.pi*radio**2
volumen=(4/3)*math.pi*radio**3

print('el area del circulo es: ',str(area))
print('el volumen del circulo es: ',str(volumen))