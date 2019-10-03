# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 23:32:39 2019

@author: Jesús García
"""
##Ejercicio: 15  "Unidades de distancia"
##En este ejercicio, creará un programa que comienza leyendo una medida en pies del usuario.
##Entonces su programa debe mostrar la distancia equivalente en pulgadas, yardas y millas.
##Use Internet para buscar los factores de conversión necesarios si no los tienes memorizados.


pies=int(input('ingrese la medida en pies: '))

pul=pies*(12/1)
yar=pies*(0.333/1.0)
milla=pies*(1/5280)

print('la didtancia de pies a pulgadas es:' +str(pul),'in')
print('la didtancia de pies a yardas es:' +str(yar),'yardas')
print('la didtancia de pies a millas es:' +str(milla),'millas')