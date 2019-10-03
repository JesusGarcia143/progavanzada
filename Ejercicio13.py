# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 23:16:07 2019

@author: Jesús García
"""
##Ejercicio: 13
##Escriba un programa que comience leyendo una cantidad de centavos del usuario como entero. 
##Luego, su programa debe calcular y mostrar las denominaciones de monedas que deberían
##usarse para dar esa cantidad de cambio al comprador.
##El cambio debe administrarse utilizando la menor cantidad de monedas posible. 
##Suponga que la máquina está cargada con centavos, monedas de cinco centavos, monedas de
## diez centavos, cuartos, locos y toonies.

##Una moneda de un dólar se introdujo en Canadá en 1987. Se conoce como Loonie porque
##un lado de la moneda tiene un loon (un tipo de pájaro). Los dos La moneda de un dólar, 
##conocida como toonie, se introdujo 9 años después. Su nombre es derivado de la 
##combinación del número dos y el nombre del loco

Toonie=200
Loonie=100
quarter=25
dime=10
nickel=5

centavos=int(input('ingrese los centavos: '))

print("", centavos // Toonie,  'Toonies')
centavos=centavos%Toonie

print("", centavos // Loonie,  'Loonies')
centavos=centavos%Loonie

print("", centavos // quarter,  'quarters')
centavos=centavos%Toonie

print("", centavos // dime,  'dimes')
centavos=centavos%dime

print("", centavos // nickel,  'nickels')
centavos=centavos%nickel
