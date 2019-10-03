# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 15:35:31 2019

@author: Jesús García
"""

edad= int(input('Inserta tu edad: ' ))

if edad > 0 and edad < 2:
    print('Eres un bebe')
elif edad >= 2 and edad < 9:
    print('Eres un niño')
elif edad >= 9 and edad < 15:
    print('Eres un adolescente')
elif edad >= 15 and edad < 25:
    print('Eres un joven')
elif edad >= 25 and edad < 45:
    print('Eres un adulto')
elif edad >= 45 and edad < 60:
    print('Eres un adulto de mediana edad')
elif edad >= 60:
    print('Eres un adulto mayor')
else:
    print('Inserta una edad valida')