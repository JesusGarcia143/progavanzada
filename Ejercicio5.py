# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 13:13:47 2019

@author: Jesús García
"""

lmenos=.10
lomas=.25
menos=int(input('¿Cuantas botellas chicas has ingresado?'))
mas=int(input('¿Cuantas botellas grandes has ingresado?'))
operacion=menos * lmenos + mas * lomas
print("Tu total es $%.2f." % operacion)