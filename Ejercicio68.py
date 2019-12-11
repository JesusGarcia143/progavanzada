# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 22:38:28 2019

@author: Jesús García
"""
##Ejercicio:  68 Bits de paridad
def get_input():
  bits = input("Bits: ")
  
  return bits
  
def division(bits):
  num = bits.count("1")
  if num % 2 == 0:
    parity = 0
  else:
    parity = 1
  
  return parity
  
def print_parity(parity):
  print("Parity bit: ", parity)
  
def main():
  bits = get_input()
  if bits != "":
    parity = division(bits)
    print_parity(parity)
  else:
    return True

while True:  
  blank_line = main()
  if blank_line == True:
    break