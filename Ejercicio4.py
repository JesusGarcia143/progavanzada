# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 15:22:18 2019

@author: Jesús García
"""
largo= float(input('Introduce el largo del campo en metros '))
ancho= float(input('Introduce el ancho del campo en metros '))
area= (largo*ancho)*(1.0/4046.856)
print('El area es: ' + str(area))
