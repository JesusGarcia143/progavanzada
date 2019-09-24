# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 15:20:51 2019

@author: Jesús García
"""

import math

di1=int(input('Ingrese el valor de distancia 1 '))
ga1=int(input('Ingrese el valor de grados 1 '))
di2=int(input('Ingrese el valor de distancia 2 '))
ga2=int(input('Ingrese el valor de grados 2 '))

g1= math.radians (ga1)
g2= math.radians (ga2)
t1= math.radians (di1) 
t2= math.radians (di2)

distancia= 6371.01 * math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2)
* math.cos(g1-g2))

print('Distancia entre los puntos' , distancia)
