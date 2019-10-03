# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 15:16:28 2019

@author: Jesús García
"""

##Ejercicio: 46
##El año esta dividido en cuatro temporadas: primavera, verano, otoño e invierno.
##Aunque las fechas exactas cambian un poco dependiendo del año, usemos las siguientes 
##fechas:

##Primavera            Marzo 21
##Verano               Junio 21
##Otoño                Septiembre 22
##Invierno             Diciembre 21

##Escriba un programa en el que el usuario introduzca el mes y el día. El usuario introducira
##el nombre del mes como una *string* seguido del día como un entero *int*. Su programa 
##debe desplegar la temporada de acuerdo a la información inytroducida por el usuario.

mes=str(input('inserta el mes: '))
dia=int(input('inserta el dia: '))

if mes =="enero" or mes=="febrero":
    temporada="invierno"
elif mes=="marzo":
    if dia<20:
        temporada="invierno"
else:
    temporada="primavera"

if mes == "abril" or mes == "mayo":
    temporada="primavera"
elif mes=="junio":
    if dia<21:
        temporada="primavera"
else:
    temporada="verano"
if mes=="julio" or mes=="agosto":
            temporada="verano"
elif mes=="septiembre":
            if dia<22:
                temporada="verano"
else:
    temporada="otoño"
if mes=="octubre" or mes=="noviembre":
                temporada="otoño"
elif mes=="diciembre":
                if dia<21:
                    temporada="otoño"
                
else:
    temporada="inverno"
                
print(mes, dia, "es en", temporada)