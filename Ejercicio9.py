# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 14:55:29 2019

@author: Jesús García
"""

#Ejercicio 9:Interés compuesto.
#Usted acaba de abrir una nueva cuenta de ahorros con el cual gana el 4% de interés por año.
#El interés que usted genera es pagado al final del año, y es agregado al balance de la 
#cuenta de banco. Escriba un programa que comienze por leer la cantidad de dinero depocitada
#en la cuenta (El usuario introduce esta cantidad). El programa debe calcular y mostrar
#la  cantidad de dinero en la cuenta despúes del primer,segundo y tercer año. Despliegue
#las cantidades de dinero redondeado a 2 decimales.

interes=0.04
deposito= float(input('Ingrese la cantidad a depositar en el año:$'))
ano1=deposito*interes 
ano1T=ano1+deposito 
print('El total en su cuenta en este ano es:$%.2f' %ano1T)

ano2=ano1T*interes
ano2T=ano1T+ano2
print('El total en su cuenta en este ano es:$%.2f' %ano2T)

ano3=ano2T*interes
ano3T=ano2T+ano3
print('El total en su cuenta en este ano es:$%.2f' %ano3T)





