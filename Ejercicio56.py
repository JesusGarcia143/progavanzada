# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 02:28:09 2019

@author: Jesús García
"""
##Ejercicio:  56 "Factura del teléfono celular"

CHAR  =  ' - '

LLAMADA  =  50
TEXTO  =  50
COSTE  =  15.00
TOTAL  =  15.00
COSTE_911  =  0.44
TAX_RATE  =  0.05

minutos =  int ( input ( ' Ingrese la cantidad de tiempo de emisión en minutos: \ t ' ))

si minutos >  50 :
  extraMinutes = minutos -  50
  extraMinutesCost = extraMinutes *  0.25
  TOTAL  + = extraMinutesCost
  
textos =  int ( input ( ' Ingrese el número de textos: \ t ' ))

si textos >  50 :
  extraTexts = textos -  50
  extraTextsCost = extraTexts *  0.15
  TOTAL  + = extraTextsCost

TOTAL  + =  COSTO_911

TAX  =  TAX_RATE  *  TOTAL
TOTAL  + =  IMPUESTO

imprimir ( CHAR  *  50 )

print ( ' Cargo base: $ % .2f '  % ( COSTE ))

prueba :
  print ( ' Cargo por minutos adicionales: $ % .2f '  % (extraMinutesCost))

excepto  NameError :
  pasar

prueba :  
  print ( ' Cargo adicional por mensajes de texto: $ % .2f '  % (extraTextsCost))

excepto  NameError :
  pasar

print ( ' 911 Fee: $ % .2f '  % ( COST_911 ))
print ( ' Impuesto: $ % .2f '  % ( IMPUESTO ))
print ( ' Total: $ % .2f '  % ( TOTAL ))