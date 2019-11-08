# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 00:39:19 2019

@author: Jesús García
"""
##Ejercicio: 32 " Ordenar 3 enteros"
##Cree un programa que lea tres enteros del usuario y los muestre ordenados
##orden (de menor a mayor). Usa las funciones min y max para encontrar el más pequeño
##y valores más grandes. El valor medio se puede encontrar calculando la suma de los tres
##valores, y luego restando el valor mínimo y el valor máximo.

uno =  int ( input ( ' Introducir el primer numero: '))
dos =  int ( input ( ' Introducir el segundo numero: '))
tres =  int ( input ( ' Introducir el tercer numero: '))

menor =  min (uno, dos, tres)
mayor =  max (uno, dos, tres)
medio = (uno + dos + tres) - menor - mayor

print ( " \ n El orden de menor a mayor es: " , menor, ' , ' , medio, ' , ' , mayor)