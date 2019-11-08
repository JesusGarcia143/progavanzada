# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 02:17:52 2019

@author: Jesús García
"""

##Ejercicio:  52 "Puntos de calificación a calificación de letra"

correct =  int ( input ( ' Ingrese el número de problemas que obtuvo correcto: ' ))

si es correcto >  0 :
    print ( '¡Lo tengo! ' )

total =  int ( input ( ' Ingrese el número total de problemas en la prueba: ' ))

si es correcto >  0 :
    print ( '¡Lo tengo! ' )
    
porcentaje = correcto / total *  100

si porcentaje <  65 :
  letra =  ' F '
  
si porcentaje >  65  y porcentaje <  70 :
  letra =  ' D '

si porcentaje >  69  y porcentaje <  80 :
  letra =  ' C '

si porcentaje > =  80  y porcentaje <  90 :
  letra =  ' B '

si porcentaje > =  90 :
  letra =  ' A '

print ( ' Su porcentaje correcto es: ' , porcentaje)

print ( ' Tu calificación de letra es: ' , letra)