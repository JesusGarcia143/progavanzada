# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 14:24:48 2019

@author: Jesús García
"""

##Ejercicio 25: Unidades de Tiempo
##Crear un programa que le pida al usuario la duración en días,horas,minutos y segundos.
##Calcular y desplegar la cantidad total de segundos de duración.

D=float(input('Ingrese los dias: '))
H=float(input('Ingrese las horas: '))
M=float(input('Ingrese los minutos: '))
S=float(input('Ingrese los segundos: '))

dias=D*86400
horas=H*3600
minutos=M*60
segundos=S

totaldesegundos= dias+horas+minutos+segundos
print('El total de segundos es: ' , totaldesegundos)
