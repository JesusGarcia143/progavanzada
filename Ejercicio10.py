# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:20:04 2019

@author: Jesús García
"""

#Cree un programa que lea dos valores enteros, a y b, introducidos por el usuario
#Su programa debe calcular y mostrar.

import math
a=float(input('Ingrese un número:'))
b=float(input('Ingrese un número:'))

suma=a+b
print('La suma de sus números es:',a,'+',b,'=',suma)
resta=b-a
print('La diferencia de sus números es:',b, '-',a,'=', resta)
multiplicacion= a*b
print('El producto de sus números es:',a,'*',b,'=', multiplicacion)
cociente=a/b
print('El cociente de sus números es:',a, '/',b, '=', cociente)
residuo= a%b
print('El residuo del cociente de sus números es:',residuo)
print('El resultado logaritmico de su primer número es:',math.log(a,10))
print('El resultado de su primer número elevado a su segundo número es:',pow(a,b))