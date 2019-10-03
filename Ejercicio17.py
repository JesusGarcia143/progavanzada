# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 23:56:04 2019

@author: Jesús García
"""
##Ejercicio: 17 "Capacidad calorífica"
##La cantidad de energía requerida para aumentar la temperatura de un gramo de material.
##en un grado Celsius es la capacidad de calor específica del material, C. La cantidad 
##total de energía requerida para elevar m gramos de un material en ΔT grados Celsius 
##puede ser calculado usando la fórmula: q = mCΔT.

##Escriba un programa que lea la masa de un poco de agua y el cambio de temperatura del 
##usuario.Su programa debe mostrar la cantidad total de energía que debe ser agregado 
##o eliminado para lograr el cambio de temperatura deseado.

##Sugerencia: La capacidad calorífica específica del agua es 4.186 J/g◦C. 
#Porque el agua tiene una densidad de 1.0 gramo por mililitro, puede usar gramos y mililitros
##indistintamente en este ejercicio.

##Extienda su programa para que también calcule el costo de calentar el agua. 
##Electricidad normalmente se factura utilizando unidades de kilovatios hora en lugar de
##julios. En este ejercicio, debe suponer que la electricidad cuesta 8,9 centavos por
##kilovatio-hora. Utilizar su programa para calcular el costo de hervir agua por una taza
##de café.

##Sugerencia: deberá buscar el factor para convertir entre julios y kilovatios hora para
##completar la última parte de este ejercicio.

import math
capagua=4.186
elec=8.9
kwh=2777*math.e**-7

volumen=float(input('ingrese la cantidad de agua: '))
temp=float(input('ingrese la tempreatura: '))

q=volumen*temp*capagua

print('Este requiere %d Joules de energia' %q)

kilo=q+kwh
cost=kilo+8.9
print('Este es el costo de la anergia: %.2f' %cost)