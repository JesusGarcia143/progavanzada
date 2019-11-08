# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 01:35:29 2019

@author: Jesús García
"""

##Ejercicio: 40 "Nombra ese triángulo"
##Un triángulo se puede clasificar en función de la longitud de sus lados como isósceles
##equiláteros o escaleno. Los 3 lados de un triángulo equilátero tienen la misma longitud. Un isósceles
##el triángulo tiene dos lados que tienen la misma longitud y un tercer lado que es 
##diferente longitud. Si todos los lados tienen diferentes longitudes, entonces el triángulo es escaleno.
##Escriba un programa que lea las longitudes de 3 lados de un triángulo del usuario.
##Muestra un mensaje que indica el tipo de triángulo.


long1 =  float ( input ( ' Inserte longitud del primer lado: '))
long2 =  float ( input ( ' Inserte longitud del segundo lado: '))
long3 =  float ( input ( ' Inserte longitud del tercer lado: '))



    long1 == long2 == long3:
	triangulo =  ' equilatero '
elif long1 == long2 o long1 == long3 o long2 == long3:
	triangulo =  " isoseles "
más :
	triangulo =  ' escaleno '
	
print ( ' Tipo de triangulo: ' , (triangulo))