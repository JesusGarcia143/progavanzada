# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 01:16:30 2019

@author: Jesús García
"""

##Ejercicio 37: "Nombra esa forma"

##Escriba un programa que determine el nombre de una forma a partir de su número de lados. Leer
##el número de lados del usuario y luego informar el nombre apropiado como parte de
##un mensaje significativo. Su programa debe admitir formas con 3
##hasta (e incluyendo) 10 lados. Si se ingresa un número de lados fuera de este rango
##entonces su programa debería mostrar un mensaje de error apropiado.


    mientras  cierto :
  s =  int ( input ( ' Ingresar número apagado 3 - 10: \ n ' ))
  a =  ' Polígono con % d lados a % s . \ n '
  si s ==  3 :
    print (a % ( 3 , ' Triángulo ' ))
  elif s ==  4 :
    print (a % ( 4 , ' Cuadrilátero ' ))
  elif s ==  5 :
    print (a % ( 5 , ' Pentágono ' ))
  elif s ==  6 :
    print (a % ( 6 , ' Hexágono ' ))
  elif s ==  7 :
    print (a % ( 7 , ' Heptagon and a septagon ' ))
  elif s ==  8 :
    print (a % ( 8 , ' Octágono ' ))
  elif s ==  9 :
    print (a % ( 9 , ' Nonagon ' ))
  elif s ==  10 :
    print (a % ( 10 , ' Decágono ' ))
  más :
    print ( ' Número de error. \ n ' )