# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 02:29:48 2019

@author: Jesús García
"""

##Ejercicio: 57 "¿Es un año bisiesto?"

mientras  cierto :
    
  año =  int ( input ( ' Ingrese el año: \ t ' ))
  
  yes =  ' % d es un año bisiesto. '  % (año)
  no =  ' % d no es un año bisiesto. '  % (año)
  
  si año %  400  ==  0 :
    imprimir (sí)
  
  año elif %  100  ==  0 :
    imprimir (no)
  
  año elif %  4  ==  0 :
    imprimir (sí)
  
  más :
    imprimir (no)
  
  print ()