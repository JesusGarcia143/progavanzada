# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 01:27:39 2019

@author: Jesús García
"""

##Ejercicio 39: Niveles de sonido

##La siguiente tabla enumera el nivel de sonido en decibelios para varios ruidos comunes.

##Nivel de decibelios de ruido (dB)
##Jackhammer 130
##Cortacésped a gas 106
##Despertador 70
##Habitación tranquila 40

##Escriba un programa que lea un nivel de sonido en decibelios del usuario. Si el usuario
##ingresa un nivel de decibelios que coincide con uno de los ruidos en la tabla y luego su programa
##debe mostrar un mensaje que contenga solo ese ruido. Si el usuario ingresa un número
##de decibelios entre los ruidos enumerados, entonces su programa debería mostrar un mensaje
##indicando entre qué ruidos se encuentra el nivel. Asegúrese de que su programa también genere
##salida razonable para un valor menor que el ruido más silencioso de la tabla, y para un
##valor mayor que el ruido más alto en la tabla.



decibelios =  flotante ( input ( " Ingrese el número de decibelios: " ))
	
si decibelios >  0  y decibelios <  40 :
    print ( ' más silencioso que una habitación silenciosa ' )
		
elif decibelios ==  40 :
    print ( ' casi lo mismo que una habitación tranquila ' )
	
elif decibelios >  40  y decibelios <  70 :
    print ( ' más silencioso que un despertador ' )
elif decibelios ==  70 :
    print ( ' casi lo mismo que un despertador ' )
		
elif decibelios >  70  y decibelios <  106 :
    print ( ' más silencioso que una cortadora de césped ' )
	
elif decibelios ==  106 :
    ( ' casi lo mismo que una cortadora de césped ' ).
	
elif decibelios >  106  y decibelios <  130 :
    print ( " más silencioso que un martillo neumático " )
		
elif decibelios ==  130 :
    print ( ' casi lo mismo que un martillo neumático ' )
		
elif decibelios >  130 :
    print ( ' demasiado fuerte ' )
		
más :
    print ( ' Ingrese un valor de datos correcto ' )
		
    print ( ' Tu nivel de sonido es ' )
