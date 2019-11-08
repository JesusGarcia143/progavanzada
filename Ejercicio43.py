# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 01:54:18 2019

@author: Jesús García
"""

##Ejercicio: 43 "Caras sobre el dinero"
##Si bien los billetes de dos dólares rara vez se ven en circulación en los Estados Unidos,
##son de curso legal que pueden gastarse como cualquier otra denominación. los
##Estados Unidos también ha emitido billetes en denominaciones de $ 500, $ 1,000,
##$ 5,000 y $ 10,000 para uso público. Sin embargo, los billetes de alta denominación
##no se han impreso desde 1945 y se suspendieron oficialmente en 1969. Como
##Como resultado, no los consideraremos en este ejercicio.

denom =  int ( input ( ' Ingresa denominación de billete: $ ' ))

nom =  " "

si denom ==  1 :
	nom =  ' George Washington '
si denom ==  2 :
	nom =  ' Thomas Jefferson '
si denom ==  5 :
	nom =  ' Abraham Lincoln '
si denom ==  10 :
	nom =  ' Alexander Hamilton '
si denom ==  20 :
	nom =  ' Andrew Jackson '
si denom ==  50 :
	nom =  ' Ulises S. Grant '
si denom ==  100 :
	nom =  ' Benjamin Franklin '
	
si nom ==  ' ' :
	print ( ' Cantidad erronea, ingresa nueva cantidad. ' )
más :
	print ( ' El personaje en la denominación es: ' , (nom))