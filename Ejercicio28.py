# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 23:00:25 2019

@author: Jesús García
"""
##Ejercicio: 28 "sensación térmica"
##Cuando el viento sopla en clima frío, el aire se siente aún más frío de lo que realmente
##es porque el movimiento del aire aumenta la velocidad de enfriamiento de los objetos
##calientes, como personas. Este efecto se conoce como sensación térmica.
##En 2001, Canadá, el Reino Unido y los Estados Unidos adoptaron el siguiente
##fórmula de bajada para calcular el índice de sensación térmica. Dentro de la fórmula 
##Ta está el La temperatura del aire en grados Celsius y V es la velocidad del viento en 
##kilómetros por hora.Se puede usar una fórmula similar con diferentes valores constantes
##con temperaturas en grados Fahrenheit y velocidades del viento en millas por hora.
##WCI = 13.12 + 0.6215Ta - 11.37V0.16 + 0.3965TaV0.16
##Escriba un programa que comience leyendo la temperatura del aire y la velocidad del 
##viento del usuario. Una vez que se hayan leído estos valores, su programa debería mostrar
##la sensación térmica índice redondeado al entero más cercano.
##El índice de enfriamiento del viento solo se considera válido para temperaturas 
##inferiores o igual a 10 grados centígrados y velocidades del viento superiores a 4,8
##kilómetros por hora.

aire =float(input('Introduce la temperatura del aire: '))
viento =float(input('Introducir la velocidad del viento: '))

sensacion_termica = 13.12+(0.6215*aire)-(11.37*(viento(0.16))^2)+(0.3965*aire)*(viento((0,16))^2)

print ( ' sensacion termica es ' , (sensacion_termica))
