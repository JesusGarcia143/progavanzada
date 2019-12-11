# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 23:50:34 2019

@author: Jesús García
"""
##Ejercicio: 97   Buena contraseña aleatoria
from ejercicio94 import randomPassword
from ejercicio96 import checkPassword

def main(): 
    n = 0
    passw = ''
    while not checkPassword(passw): 
        passw = randomPassword()
        n = n+1
    print("Intentos: ", n)
    print("Password: ", passw)
    
main()