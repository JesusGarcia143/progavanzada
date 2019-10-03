# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 00:08:42 2019

@author: Jesús García
"""
##Ejercicio: 18 "Volumen de un cilindro"
##El volumen de un cilindro se puede calcular multiplicando el área de su circular
##base por su altura. Escriba un programa que lea el radio del cilindro, junto con
##su altura, desde el usuario y calcula su volumen. Mostrar el resultado redondeado a uno
##decimal.

import math
radio=float(input('ingrese el radio del cilindro: '))
altura=float(input('ingrese la altura del cilindro: '))

volumen=(math.pi*radio**2)*(altura)

print('el volumen del cilindro es: %.1f'%volumen)