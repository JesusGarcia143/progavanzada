# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 15:38:58 2019

@author: Jesús García
"""
#Ejercicio 6:Hacer un programa en el que el usuariointroduzca el nombre de la
#comida que ordeno en un restaurante y precio despues su programa debe calcular elsub total
#el iva y la propina de toda la cuenta. La salida del programa debe parecerse a un ticket
#de restaurante, use un iva del 16% y una propina del 15% del subtotal
#los valores numericos deben tener 2 decimales.
A= str(input('Introduzca el nombre de la comida: '))
a= float(input('Introduzca el valor de la comida '))

B= str(input('Introduzca el nombre de la comida: '))
b= float(input('Introduzca el valor de la comida '))

C= str(input('Introduzca el nombre de la comida: '))
c= float(input('Introduzca el valor de la comida '))

D= str(input('Introduzca el nombre de la comida: '))
d= float(input('Introduzca el valor de la comida '))

E= str(input('Introduzca el nombre de la comida: '))
e= float(input('Introduzca el valor de la comida '))







print('--------------------------------------')
subtotal=a+b+c+d+e
print('subtotal: $%.2f ' % subtotal)
iva= subtotal*0.16
print('iva: $%.2f ' % iva )
propina= subtotal* 0.15
print('propina: $%.2f ' % propina)

print('-------------------------')
print('              total')
print('-------------------------')
total=subtotal+iva+propina
print('total: $%.2f' % total)




