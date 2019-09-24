# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 14:42:58 2019

@author: Jesús García
"""

#Ejercicio 8: Un vendedor de una página de abarrotes en línea vende dos tipos de cajas de 
#cereal. CornFlakes de 750gr y Trix de 500gr. Escriba un programa que lea el número de cajas
#de CornFlakes y cajas Trix, cuyo valor debe ser introducido por el usuario. Despues su
#programa debe calcular y mostrar el total del peso (en kilogramos) del envio

caja1=0.750
caja2=0.500
CornFlakes= int(input('Ingrese la cantidad de cajas de CornFlakes: '))
Trix= int(input('Ingrese la cantidad de cajas de Trix: '))
  
Peso1= CornFlakes*caja1
peso2= Trix*caja2
PesoT= Peso1+peso2
print('El peso total a enviar es:' , PesoT, 'kg')