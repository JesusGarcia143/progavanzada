# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 02:25:37 2019

@author: Jesús García
"""

##Ejercicio: 55 "frecuencia para nombrar"


frecuencia =  flotante ( entrada ( ' Ingrese la frecuencia: ' ))

categoría =  ' '

si frecuencia <  3e9 :
	categoría =  ' ondas de radio '
frecuencia elif > =  3e9  y frecuencia <  3e12 :
	categoría =  ' microondas '
frecuencia elif > =  3e12  y frecuencia <  4.3e14 :
	categoría =  ' luz infrarroja '
frecuencia elif > =  4.3e14  y frecuencia <  7.5e14 :
	categoria =  ' luz visible '
frecuencia elif > =  7.5e14  y frecuencia <  3e17 :
	categoría =  ' luz ultravioleta '
frecuencia elif > =  3e17  y frecuencia <  3e19 :
	categoría =  ' rayos X '
frecuencia elif > =  3e19 :
	categoría =  ' rayos gamma '
	
if category ! =  ' ' :
	print ( ' La frecuencia es categoría: ' , (categoría))
más :
	print ( ' La frecuencia ingresada no es válida ' )