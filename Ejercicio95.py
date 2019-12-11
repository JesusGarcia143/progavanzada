# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 23:46:28 2019

@author: Jesús García
"""
##Ejercicio: 95   Matrícula Aleatoria
import random as rand

def license_gen():
    set_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    set_numbers = [1,2,3,4,5,6,7,8,9,0]
    lenght = rand.randint(3,4)
    licen_numbs = rand.sample(set_numbers,lenght)
    licen_letts = rand.sample(set_letters,3)
    licen = ''
    if lenght == 3: 
        for i in licen_letts:
            licen = licen + i
        for i in licen_numbs: 
            licen = licen + str(i)
    elif lenght == 4: 
        for i in licen_numbs:
            licen = licen + str(i)
        for i in licen_letts: 
            licen = licen + i    
    print(licen)
    return licen

def main():
    license_gen()

main()  