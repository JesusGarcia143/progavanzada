# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 15:50:36 2019

@author: Jesús García
"""
##Ejercicio: 49 'Escala de Richter'
##La siguiente tabla contiene rangos de magnitud de terremotos en la escala de Richter y
##sus descriptores:
##Magnitude                     Descriptor
##Less than 2.0                  Micro
##2.0 to less than 3.0          Very minor
##3.0 to less than 4.0          Minor
##4.0 to less than 5.0          Light
##5.0 to less than 6.0          Moderate
##6.0 to less than 7.0          Strong
##7.0 to less than 8.0          Major
##8.0 to less than 10.0         Great
##10.0 or more                  Meteoric

##Escriba un programa que lea la admiración del usuario y muestre la información apropiada.
##descriptor como parte de un mensaje significativo. Por ejemplo, si el usuario ingresa 5.5 entonces
##su programa debe indicar que un terremoto de magnitud 5.5 se considera
##terremoto moderado.

m=float(input('Inserte la magnitud de su temblor: '))
if m == 2:
    print('micro')
elif m >= 2.0 and m < 2.9:
    print('un terremoto de magnitud' , m, 'se considera un terremoto muy menor')
elif m >= 3.0 and m <=3.9:
    print('un terremoto de magnitud' ,m, 'se considera un terremoto menor')
elif m >= 4.0 and m <= 4.9:
    print('un terremoto de magnitud' ,m, 'se considera un terremoto ligero')
elif m >= 5.0 and 5.9:
    print('un terremoto de magnitud' ,m, 'se considera un terremoto moderado')
elif m >= 6.0 and 6.9:
    print('un terremoto de magnitud' ,m, 'se considera un terremoto fuerte')
elif m >= 7.0 and 7.9:
    print('un terremoto de magnitud' ,m, 'se considera un terremoto mayor')
elif m >= 8.0 and 9.9:
    print('un terremoto de magnitud' ,m, 'se considera un terremoto excedente')
elif m >= 10.0:
    print('un terremoto de magnitud' ,m,'se considera un terremoto menor meteórico')