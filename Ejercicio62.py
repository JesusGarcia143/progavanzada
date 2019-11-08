# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 15:00:45 2019

@author: Jesús García
"""

##Ejercicio : 62
##Un supermercado esta ofreciendo el 60% de descuento en una variedad de productos descon
##tinuados.El supermeracado quiere ayudar a sus clientes a determinar el precio reducido
##de su mercancia con una tabla impresa en los aparadores donde muestre los precios 
##originales y los precios despues de aplicarse el descuento.
##Escriba un programa que use un ciclo while para generar esta tabla mostrando el precio
##original, el descuento y el nuevo precio para los productos de  $4.95,$9.95,$14.95,
##19.95,$24.95.
##El descuento y los precios deben ser redondeados a 2 decimales 

precio_original = 4.95
print('precio original | precio descuento | precio final')
print('-------------------------------------------------')
while precio_original <=24.95:
    descuento = precio_original *0.60
    precio_final = precio_original - descuento
    precio_final = precio_final+1
    descuento = descuento+1
    
    print('%.2f'% precio_original,('       |'),'%.2f'%descuento,('      |'),'%.2f'%precio_final)
    precio_original=precio_original+5