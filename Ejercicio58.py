# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 02:33:58 2019

@author: Jesús García
"""

##Ejercicio: 58 "al día siguiente"

año =  int ( input ( ' Ingresar año: ' ))
mes =  int ( input ( ' Ingrese mes: ' ))
day =  int ( input ( ' Ingresar día: ' ))

next_year = year
next_month = month
next_day = day

si mes ! =  12 :
	next_year = year
más :
	si día ! =  31 :
		next_day = año
	más :
		siguiente_año = año +  1
		
# Sep, abril, junio, noviembre solo tienen 30 días

si mes ! =  9  y mes ! =  4  y mes ! =  6  y mes ! =  6  y mes ! =  11 :
	si día ! =  31 :
		next_month = month
		next_day = day +  1
	más :
		si mes ! =  12 :
			next_month = mes +  1
		más :
			next_month =  1
		next_day =  1
más :
	si día ! =  30 :
		next_month = month
		next_day = day +  1
	más :
		si mes ! =  12 :
			next_month = mes +  1
		más :
			next_month =  1
		next_day =  1
		
si mes ! =  2 :
	salto =  verdadero

	si año %  400  ==  0 :
		salto =  verdadero
	elif año %  100  ==  0  y  no año %  400  ==  0 :
		salto =  falso 
	elif año %  4  ==  0  y  no año %  100  ==  0  y  no año %  400  ==  0 :
		salto =  verdadero 
	
	si día ==  28 :
		si salto:
			next_month = month
			next_day = day +  1
		más :
			next_month = mes +  1
			next_day =  1
			
	más :
		next_month = month
		next_day = day +  1
		
print ( ' El día siguiente es: ' , next_year, ' - ' , next_month, ' - ' , next_day)