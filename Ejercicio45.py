# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 02:00:35 2019

@author: Jesús García
"""

##Ejercicio: 45 "¿De qué color es ese cuadrado?"

mientras  cierto :  
  oddSet = [ ' a ' , ' c ' , ' e ' , ' g ' ]
  evenSet = [ ' b ' , ' d ' , ' f ' , ' h ' ]
  números impares = [ 1 , 3 , 5 , 7 ]
  números pares = [ 2 , 4 , 6 , 8 ]
  letra =  entrada ( ' Ingrese la letra: \ n ' )
  mientras  cierto :  
    prueba :
      número =  int ( input ( ' Ingrese el número: \ n ' ))
      rotura
    excepto  ValueError :
      print ( 'El número tiene que ser un entero. \ n ' )
  if letter.lower () en oddSet y number en oddNumbers:
    print ( ' El cuadrado es negro. \ n ' )
  elif letter.lower () en evenSet y number en oddNumbers:
    print ( ' El cuadrado es blanco. \ n ' )
  elif letter.lower () en evenSet y number en evenNumbers:
    print ( ' El cuadrado es negro. \ n ' )
  elif letter.lower () en oddSet y number en evenNumbers:
    print ( ' El cuadrado es blanco. \ n ' )
  más :
    print ( 'La letra tiene que ser una letra. \ n ' )