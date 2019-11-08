# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 01:23:21 2019

@author: Jesús García
"""

##Ejercicio 38: Nombre del mes a Número de días

##La duración de un mes varía de 28 a 31 días. En este ejercicio crearás
##un programa que lee el nombre de un mes del usuario como una cadena. Entonces tu
##programa debe mostrar el número de días en ese mes. Mostrar "28 o 29 días"
##para febrero para que se aborden los años bisiestos.



print ( ' Lista de meses: enero, febrero, marzo, abril, mayo, junio, julio, agosto, septiembre, octubre, noviembre, diciembre ' )

mes_nombre =  input ( " Ingrese el nombre del mes: " )

if mes_nombre ==  ' febrero ' :
	print ( ' No. de días: 28/29 días ' )
 elif mes_nombre en ( ' abril ' , ' junio ' , ' septiembre ' , ' noviembre ' ):
	print ( ' No. de días: 30 días ' )
elif mes_nombre en ( ' enero ' , ' marzo ' , ' mayo ' , ' julio ' , ' agosto ' , ' octubre ' , ' diciembre ' ):
	print ( ' No. de días: 31 días ' )
más :
	print ( ' Nombre del mes de error ' )