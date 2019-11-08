# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 14:14:56 2019

@author: Jesús García
"""

##Ejercicio:78
## Escriba un programa que convierta un número decimal (base 10) que inserte un usuario comó
##número entero y despúes use el logaritmo de división mostrado  para realizar la conversión.
##Cuando el algoritmo se complete el resultado se deberá contener la representación del 
##número en binario.Despúes se deberá desplegar el resultado con el mensaje apropiado.

##Sea resultado una variable string vacia sea q un número entero a convertir repetir:
##*Sea r igual al residuo cuando q es dividido entre 2
##*Convertir r a string y agregarlo al comienzo de resultado
##*Dividir q entre 2,eliminar cualquier residuo y guardar el resultado de nuevo en q.
##hasta que q sea cero.

n= int(input('Ingrese el número que desea convertir: ' ))
resultado=''
resultado= n % 2
String= (resultado)
print(resultado) 