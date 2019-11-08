# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 02:22:00 2019

@author: Jesús García
"""
##Ejercicio: 54 "longitudes de onda de luz visible"
##Escriba un programa que lea una longitud de onda del usuario e informe su color. Monitor
##un mensaje de error apropiado si la longitud de onda ingresada por el usuario está fuera de
##espectro visible.
VIOLETA  =  380
AZUL  =  450
VERDE  =  495
AMARILLO  =  570
NARANJA  =  590
ROJO  =  620
TOP  =  750

WAVELENGTH  =  ' El color es % s . '

times =  int ( input ( ' ¿Cuántas veces deseas ejecutar este programa ?: \ n ' ))

para recuento en  rango ( 1 , veces +  1 ):
  mientras  cierto :
    print ( ' \ n Time % d \ n '  % (count))
  
    wavelength =  int ( input ( ' Ingrese la longitud de onda en nanómetros. Elija 380 - 750: \ n ' ))
    
    si  VIOLETA  <= longitud de onda <  AZUL :
      print ( WAVELENGTH  % ( ' Violeta ' ))
      rotura
    
    elif  AZUL  <= longitud de onda <  VERDE :
      print ( WAVELENGTH  % ( ' Azul ' ))
      rotura
    
    elif  VERDE  <= longitud de onda <  AMARILLO :
      print ( WAVELENGTH  % ( ' Verde ' ))
      rotura
    
    elif  AMARILLO  <= longitud de onda <  NARANJA :
      print ( WAVELENGTH  % ( ' Amarillo ' ))
      rotura
    
    elif  NARANJA  <= longitud de onda <  ROJO :
      print ( WAVELENGTH  % ( ' Naranja ' ))
      rotura
    
    elif  RED  <= longitud de onda <  TOP :
      print ( WAVELENGTH  % ( ' Rojo ' ))
      rotura
    
    más :
      print ( ' Elija 380 - 750. \ n ' )