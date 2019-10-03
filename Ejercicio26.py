# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 00:23:37 2019

@author: Jesús García
"""
##Ejercicio: 26 "Unidades de tiempo (de nuevo)"
##En este ejercicio ested revertira el proceso descrito en el ejercicio previo.
##Desarrolle un programa que comience por leer una cantidad de segundos introducidos 
##por el usuario. Su programa debe desplegar la cantidad equivalente en la forma
##D:HH:MM:SS donde D son los dias, HH so las horas, MM son los minutos y SS son los segundos.
##Las horas, minutos y segundos deben de estar en formato de dos digitos con un 0 al
##inicio, si es necesario.

segundos=int(input('Introduce la cantidad de segundos: '))
SEGUNDOS_POR_DIA=86400
SEGUNDOS_POR_HORA=3600
SEGUNDOS_POR_MINUTO=60

dias=segundos/SEGUNDOS_POR_DIA
segundosdias=segundos%SEGUNDOS_POR_DIA

horas=segundos/SEGUNDOS_POR_HORA
segundoshora=segundos%SEGUNDOS_POR_HORA

minutos=segundos/SEGUNDOS_POR_MINUTO
segundosminutos=segundos%SEGUNDOS_POR_MINUTO

print('','%00.d'% dias,':','%00.d'% horas,':','%00.d'% minutos,':','%00.d'% segundosminutos,)