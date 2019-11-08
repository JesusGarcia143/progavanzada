# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 00:04:37 2019

@author: Jesús García
"""
##Ejercicio: 29 "Celsius a Fahrenheit y Kelvin"
##Escriba un programa que comience leyendo la temperatura del usuario en grados
##Celsius. Entonces su programa debe mostrar la temperatura equivalente en grados
##Fahrenheit y grados Kelvin. Los cálculos necesarios para convertir entre diferentes
##unidades de temperatura se pueden encontrar en internet.

tem_celsius =  float ( input ( ' Introducir la temperatura en celsius: ' ))

tem_fahrenheit = tem_celsius * ( 9 / 5 ) +  32
tem_kelvin = tem_celsius +  273,15

print ( ' \ n En Fahrenheit: % .2f '  % (tem_fahrenheit))
print ( ' \ n En Kelvin: ' , (tem_kelvin))