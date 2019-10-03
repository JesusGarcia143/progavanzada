# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 15:01:48 2019

@author: Jesús García
"""

##Ejercicio 19:Escriba un programa que determine como un objeto viaja cuando golpea el piso.
##El usuario insertará la información de la altura desde donde el objeto se deja caer, en me
##tros(m).Dado que el objeto se deja caer desde el reposo (velocidad inicial v0=0m/s).
##Asumiendo que la aceleración debido a la gravedad es de 9.81 m/s^2 y usando la fórmula
##vf=v0^2+2gd1/2. Calcule la velocidad final vf usando la velocidad inicial v0 la aceleracion
##g y la distancia d.

import math
alt=int(input('Introduce la altura=  '))
t=((2)*(9.81))*alt
vf=math.sqrt(0+t)
print('Tu velocidad final es= %.2f' %vf)
