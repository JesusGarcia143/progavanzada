# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 22:06:47 2019

@author: Jesús García
"""

print('Celsius', 'Fahrenheit')

for num in range(1, 11):
    celsius = num * 10
    print(celsius, end='      ')
    fahrenheit = 1.8 * celsius + 32
    print(fahrenheit, end=' ')
    print('\n')