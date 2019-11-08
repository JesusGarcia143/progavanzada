# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 00:23:56 2019

@author: Jesús García
"""
##Ejercicio: 30 "Unidades de presion"
##En este ejercicio creará un programa que lee la presión del usuario en kilo-
##pascales Una vez que se ha leído la presión, su programa debe informar el equivalente
##presión en libras por pulgada cuadrada, milímetros de mercurio y atmósferas. Utilizar
##sus habilidades de investigación para determinar los factores de conversión entre estas
##unidades.

KPal = float(input('Introducir la presion en kilo-pascales: '))

PSI  = KPal *  0.145037738
mercurio = KPal *  7.50062
atm = KPal /  101,3

print ( ' / n En Libras por pulgada ^ 2: % .3f ' % ( PSI ), ' (PSI) ' )
print ( ' / n En Millimetros de Mercury: % .3f ' % (mercurio), ' (mmHg) ' )
print ( ' / n En Atmosferas: % .3f ' % (atm), ' (atm) ' )