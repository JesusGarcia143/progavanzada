# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 01:50:31 2019

@author: Jesús García
"""

##Ejercicio:  42 "Frecuencia a tener en cuenta"


frecuencia =  float ( input ( ' Inserta frecuencia en Hz: '))

nota =  ' '

si frecuencia >  261.63  -  1  y frecuencia <  261.63  +  1 :
	nota =  ' C '
elif frecuencia >  293.66  -  1  y frecuencia <  293.66  +  1 :
	nota =  ' D '
frecuencia elif >  329.63  -  1  y frecuencia <  329.63  +  1 :
	nota =  ' E '
elif frecuencia >  349.23  -  1  y frecuencia <  349.23  +  1 :
	nota =  ' F '
elif frecuencia >  392.00  -  1  y frecuencia <  392.00  +  1 :
	nota =  ' G '
frecuencia elif >  440.00  -  1  y frecuencia <  440.00  +  1 :
	nota =  ' A '
elif frecuencia >  493.88  -  1  y frecuencia <  493.88  +  1 :
	nota =  ' B '
si nota ==  ' ' :
	print ( ' Esta no es una nota que corresponde con la frecuencia ' )
más :
	print ( ' La frecuencia es ' , (Nota))