# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 02:35:51 2019

@author: Jesús García
"""

##Ejercicio: 59 "¿es válida una matrícula?"

string =  input ( ' Ingrese la cadena: ' )

superior =  falso
alfa =  falso
viejo =  falso
nuevo =  falso

if string [ 0 ] .isupper () ==  True  y string [ 1 ] .isupper () ==  True  y string [ 2 ] .isupper () ==  True :
  upper =  verdadero
  

if string [ 0 ] .isalpha () ==  True  y string [ 1 ] .isalpha () ==  True  y string [ 2 ] .isalpha () ==  True  y string [ 3 ] .isdigit () ==  True  y string [ 4 ] .isdigit () ==  Verdadero  y cadena [ 5 ] .isdigit () ==  Verdadero  y superior ==  Verdadero :
  viejo =  verdadero
  
  print ( ' Esa es una placa vieja ' )


if string [ 0 ] .isdigit () ==  True  y string [ 1 ] .isdigit () ==  True  y string [ 2 ] .isdigit () ==  True  y string [ 3 ] .isdigit () ==  True :
  dígito =  verdadero

if string [ 4 ] .isalpha () ==  True  y string [ 5 ] .isalpha () ==  True  y string [ 6 ] .isalpha () ==  True :
  alfa =  verdadero

if string [ 4 ] .isupper () ==  True  y string [ 5 ] .isupper () ==  True  y string [ 6 ] .isupper () ==  True :
  upper2 =  verdadero

si alpha ==  True  y upper2 ==  True  y digit ==  True :
  nuevo =  verdadero
  
  print ( ' Esa es una nueva placa ' )

si antiguo ==  Falso  y nuevo ==  Falso :
    
  print ( ' Eso no es matrícula ' )