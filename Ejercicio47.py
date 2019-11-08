# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 15:40:14 2019

@author: Jesús García
"""

##Ejercicio: 47 'Fecha de Nacimiento al Signo Astrológico'
##Los horóscopos comúnmente reportados en los periódicos usan la posición del sol en el
##momento del nacimiento para intentar predecir el futuro. Este sistema de astrología divide
##el año en doce signos del zodiaco, como se describe en la tabla a continuación:
##Escriba un programa que le pida al usuario que ingrese su mes y día de nacimiento. 
##Entonces su programa debe informar el signo del zodiaco del usuario como parte de una
##salida adecuada mensaje.

mes_nacimiento = input("Ingrese el mes en que nació: ")
día_nacimiento = int(input("Ingrese el día en que nació: "))

if mes_nacimiento == "diciembre" and día_nacimiento >= 22 and día_nacimiento <= 31 or  mes_nacimiento == "enero" and día_nacimiento >= 1 and día_nacimiento <= 19 :
  print("Su signo zodiacal es Capricornio")

elif mes_nacimiento == "enero" and día_nacimiento >= 19 and día_nacimiento <= 31 or  mes_nacimiento == "febrero" and día_nacimiento >= 1 and día_nacimiento <= 18 :
  print("Su signo zodiacal es Acuario")

elif mes_nacimiento == "febrero" and día_nacimiento >= 19 and día_nacimiento <= 30 or  mes_nacimiento == "marzo" and día_nacimiento >= 1 and día_nacimiento <= 20 :
  print("Su signo zodiacal es Piscis")

elif mes_nacimiento == "marzo" and día_nacimiento >= 21 and día_nacimiento <= 31 or  mes_nacimiento == "abril" and día_nacimiento >= 1 and día_nacimiento <= 19 :
  print("Su signo zodiacal es Aries ")

elif mes_nacimiento == "abril" and día_nacimiento >= 20 and día_nacimiento <= 31 or  mes_nacimiento == "mayo" and día_nacimiento >= 1 and día_nacimiento <= 20 :
  print("Su signo zodiacal es Tauro")

elif mes_nacimiento == "mayo" and día_nacimiento >= 21 and día_nacimiento <= 30 or  mes_nacimiento == "junio" and día_nacimiento >= 1 and día_nacimiento <= 20 :
  print("Su signo zodiacal es Geminis")

elif mes_nacimiento == "junio" and día_nacimiento >= 21 and día_nacimiento <= 30 or  mes_nacimiento == "julio" and día_nacimiento >= 1 and día_nacimiento <= 22 :
  print("Su signo zodiacal es Cancer")

elif mes_nacimiento == "julio" and día_nacimiento >= 23 and día_nacimiento <= 30 or  mes_nacimiento == "agosto" and día_nacimiento >= 1 and día_nacimiento <= 22 :
  print("Su signo zodiacal es Leo")

elif mes_nacimiento == "agosto" and día_nacimiento >= 23 and día_nacimiento <= 31 or  mes_nacimiento == "septiembre" and día_nacimiento >= 1 and día_nacimiento <= 22 :
  print("Su signo zodiacal es Virgo")

elif mes_nacimiento == "septiembre" and día_nacimiento >= 23 and día_nacimiento <= 31 or  mes_nacimiento == "octubre" and día_nacimiento >= 1 and día_nacimiento <= 22 :
  print("Su signo zodiacal es Libra")

elif mes_nacimiento == "octubre" and día_nacimiento >= 24 and día_nacimiento <= 31 or  mes_nacimiento == "noviembre" and día_nacimiento >= 1 and día_nacimiento <= 21 :
  print("Su signo zodiacal es Scorpio")

else:
  print("Su signo zodiacal es Sagitario")