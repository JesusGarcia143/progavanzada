# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 23:27:55 2019

@author: Jesús García
"""
##Ejercicio: 87 Centrar una cadena en la terminal

WIDTH = 80

def centro(s, width):
    if width < len(s):
        return s
    
    espacios = (width - len(s)) // 2
    resultado = ' ' * espacios + s

    return resultado

def main():
    print(centro(' una fabulosa historia', WIDTH))
    print(centro('por: ', WIDTH))
    print(centro('algunos famosos', WIDTH))
    print()
    print('Una vez en el timpo...')
main()