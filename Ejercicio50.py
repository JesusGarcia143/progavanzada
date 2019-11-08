# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 02:10:14 2019

@author: Jesús García
"""

##Ejercicio 50: Raíces de una función cuadrática

matemáticas de importación

times =  int ( input ( ' Ingrese el número de veces: \ n ' ))

para recuento en  rango (tiempos):
  mientras  cierto :  
    prueba :
      a =  int ( input ( ' Ingrese el valor a: \ n ' ))
      b =  int ( input ( ' Ingrese el valor b: \ n ' ))
      c =  int ( input ( ' Ingrese el valor c: \ n ' ))
      discriminante = b **  2  -  4  * a * c
      si discriminante <  0 :
        print ( ' Número de raíces: 0 \ n ' )
      Elif discriminante ==  0 :
        raíz = ( - b + math.sqrt (discriminante)) / ( 2  * a)
        print ( ' Número de raíces: 1 \ n Raíz: % f \ n '  % (raíz))
      discriminante elif >  0 :
        root1 = ( - b + math.sqrt (discriminante)) / ( 2  * a)
        root2 = ( - b - math.sqrt (discriminante)) / ( 2  * a)
        print ( ' Número de raíces: 2 \ n Raíces: % f , % f \ n '  % (root1, root2))
      rotura
    excepto  ValueError :
      print ( ' Entrada inválida. \ n ' )

blah =  input ( ' Presione ENTER para salir. ' )