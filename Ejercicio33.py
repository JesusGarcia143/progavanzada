# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 00:47:49 2019

@author: Jesús García
"""
##Ejercicio: 33 "Pan de un día"
##Una panadería vende hogazas de pan por $ 3.49 cada una. El pan de un día tiene un descuento
##de 60 por ciento. Escriba un programa que comience leyendo la cantidad de panes de un 
##día pan que se compra al usuario. Entonces su programa debe mostrar el regular
##precio del pan, el descuento porque tiene un día y el precio total. Toda la
##los valores deben mostrarse con dos decimales y los puntos decimales en todos
##de los números deben alinearse cuando el usuario ingresa valores razonables.

undia =  int ( input ( ' Introducir la cantidad de pan que comprara: '))
regular = undia *  3.49
preciodes = undia * ( 3.49  *  0.60 )
total = regular - preciodes
print ( " El precio normal es: $ % 5.2f "  % (regular))
print ( " El descuento de un dia: $ % 5.2f "  % (preciodes))
print ( " El total a pagar es: $ % 5.2f "  % (total))