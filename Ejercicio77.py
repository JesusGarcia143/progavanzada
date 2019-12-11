# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 23:08:35 2019

@author: Jesús García
"""
##Ejercicio: 77 Binario a decimal
b_num = list(input('Input a binary number:'))
value = 0

for i in range(len(b_num)):
	digit = b_num.pop()
	if digit == '1':
		value = value + pow(2, i)
print('The decimal value of the number is', value)