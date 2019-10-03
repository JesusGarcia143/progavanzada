# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 23:26:34 2019

@author: Jesús García
"""
##Ejercicio: 14 "Unidades de altura"
##Muchas personas piensan en su altura en pies y pulgadas, incluso en algunos países que
##utiliza principalmente el sistema métrico. Escriba un programa que lea un número de pies
##de el usuario, seguido de varias pulgadas. Una vez que se leen estos valores, su programa
##debe calcular y mostrar el número equivalente de centímetros.

##Sugerencia: un pie mide 12 pulgadas. Una pulgada es 2.54 centímetros.

pies=int(input('ingrese el numero de pies: '))
pulgadas=int(input('ingrese el numero de pulgadas: '))

pies2=pies*(1/0.0328084)
pul2=pulgadas*((25.4/1)*(1/10))

print('la altura de pies a centimetros es:'+str(pies2),'cm')
print('la altura de pulgadas a centimetros es:'+str(pul2),'cm')