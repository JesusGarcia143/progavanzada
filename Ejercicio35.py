# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 14:17:53 2019

@author: Jesús García
"""

##Ejercicio: 35 "Años Perro"
##Se dice comúnmente que un año humano es equivalente a 7 años de perro. Sin embargo esto
##la conversión simple no reconoce que los perros alcanzan la edad adulta en aproximadamente 
##dos años. Como resultado, algunas personas creen que es mejor contar cada uno de los dos 
##primeros años humanos como 10.5 años de perro, y luego cuente cada año humano adicional como 4 perros
##años.

Edadhumana= int(input('Introduce la edad humana: '))
if Edadhumana < 0:
    print('Edad en un número positivo')
    exit()
elif Edadhumana <= 2:
    dedad= Edadhumana*10.5
else: 
    dedad=21+(Edadhumana-2)*4
print('Edad del perro en humanos',dedad)