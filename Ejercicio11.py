# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:35:26 2019

@author: Jesús García
"""

#Eficiencia de compustible
#En los Estados Unidos , la eficiencia del combustible para vehículos normalmente
#se expresa en millas por galón.
#En México,la eficiencia del combustible normalmente se expresa en litros por cien 
#kilómetros (L/100km).
#Usa tus habilidades de investigación para determinar como convertir de MPG A L/100km.
#Lee un programa que lea un valor del usuario en América unidades y muestra la eficiencia 
#de combustible equivalente en unidades Mexicanas

EUA=float(input('Ingrese el valor de la eficiencia en millas por galon a convertir: '))
con= EUA * 235.21
print('\n\nEl valor de la eficiencia en unidades mexicanas es:','%.2f' 'L/1OO km' % con )