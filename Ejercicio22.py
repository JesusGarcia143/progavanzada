# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 00:37:16 2019

@author: Jesús García
"""
##Ejercicio: 22 "Área de un triángulo (de nuevo)"
##En el ejercicio anterior, creó un programa que calculaba el área de un triángulo
##cuando se conocía la longitud de su base y su altura. También es posible calcular
##El área de un triángulo cuando se conocen las longitudes de los tres lados. Deje s1,s2 
##y s3 ser la longitud de los lados. Sea s = (s1 + s2 + s3) / 2. Entonces el área del 
##triángulo se puede calcular usando la siguiente fórmula: área = sqrt s × (s - s1)
##× (s - s2) × (s - s3). Desarrolle un programa que lea las longitudes de los lados 
##de un triángulo del usuario y Muestra su área.

import math

S1=int(input('Introduce la primer distancia del triangulo: '))
S2=int(input('Introduce la segunda distancia del triangulo: '))
S3=int(input('Introduce la tercer distancia del triangulo: '))
S=(S1+S2+S3)/2
Area=math.sqrt(S*(S-S1)*(S-S2)*(S-S3))

print('El area del triangulo es de: ',Area)
