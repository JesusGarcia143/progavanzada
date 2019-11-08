# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 01:42:41 2019

@author: Jesús García
"""
##Ejercicio: 41 "Nota a frecuencia"
##La siguiente tabla enumera una octava de notas musicales, comenzando con C central, a lo largo
##con sus frecuencias
##Note Frequency (Hz)
##C4 261.63
##D4 293.66
##E4 329.63
##F4 349.23
##G4 392.00
##A4 440.00
##B4 493.88
##Una vez que tenga su programa funcionando correctamente para las notas enumeradas anteriormente,
##debería agregar soporte para todas las notas de C0 a C8. Si bien esto podría hacerse por
##agregando muchos casos adicionales a su declaración if, tal solución es engorrosa,
##inelegante e inaceptable para los propósitos de este ejercicio. En cambio, deberías
##explotar la relación entre notas en octavas adyacentes. En particular, la frecuencia
##de cualquier nota en octava n es la mitad de la frecuencia de la nota correspondiente en octava n + 1.
##Al usar esta relación, debería poder agregar soporte para las notas adicionales
##sin agregar casos adicionales a su declaración if.

nombre =  input ( ' Inserta el nombre de la nota: ' )


nota = nombre [ 0 ] .upper ()

octava =  int (nombre [ 1 ])

frecuencia =  - 1

si nota ==  " C " :
	frecuencia =  261.63
elif nota ==  " D " :
	frecuencia =  293.66
elif nota ==  " E " :
	frecuencia =  329.63
elif nota ==  " F " :
	frecuencia =  349.23
elif nota ==  " G " :
	frecuencia =  392.00
elif nota ==  " A " :
	frecuencia =  440.00
elif nota ==  " B " :
	frecuencia =  493.88
	
frecuencia / =  2  ** ( 4  - octava)
	
print ( ' La nota es: ' , nota, ' frequencia es ' , (frequencia), ' Hz ' )