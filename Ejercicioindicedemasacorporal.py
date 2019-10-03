# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 14:16:17 2019

@author: Jesús García
"""

##Calculadora de IMC

masa= float(input('Inserte su masa en kg: '))
estatura= float(input('Inserte su estatura en metros: '))

imc= masa/estatura**2

if imc < 16:
    print('Tiene delgadez severa')
    
elif imc >= 16 and imc < 17:
    print('Tiene delgadez moderada')
    
elif imc >= 17 and imc < 18.5:
    print('Tiene delgadez leve')
    
elif imc >= 18.5 and imc < 25:
    print('Tiene un IMC normal')
    
elif imc >= 25 and imc < 30:
    print('Tiene preobecidad')
    
elif imc >= 30 and imc < 35:
    print('Tiene obecidad leve')
    
elif imc >= 35 and imc < 40:
    print('Tiene obecidad media')
    
elif imc >= 40:
    print('Tiene obecidad morbida')
    
else:
    print('Opción invalida')
    
print('Su imc fue de ', imc)