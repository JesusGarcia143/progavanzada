# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 02:06:24 2019

@author: Jesús García
"""
##Ejercicio: 48 "Signo Sodiacal Chino"
##Escriba un programa que lea un año del usuario y muestre el animal asociado
##con ese año Su programa debería funcionar correctamente durante cualquier año mayor o igual
##a cero, no solo los que figuran en la tabla.
##año =  int ( input ( ' Ingrese su año de nacimiento: ' ))
if (año -  2000 ) %  12  ==  0 :
    signo =  ' Dragón '
elif (año -  2000 ) %  12  ==  1 :
    signo =  ' Serpiente '
elif (año -  2000 ) %  12  ==  2 :
    signo =  ' Caballo '
elif (año -  2000 ) %  12  ==  3 :
    signo =  ' oveja '
elif (año -  2000 ) %  12  ==  4 :
    signo =  ' mono '
elif (año -  2000 ) %  12  ==  5 :
    signo =  ' gallo '
elif (año -  2000 ) %  12  ==  6 :
    signo =  ' Perro '
elif (año -  2000 ) %  12  ==  7 :
    sign =  ' Pig '
elif (año -  2000 ) %  12  ==  8 :
    signo =  ' Rata '
elif (año -  2000 ) %  12  ==  9 :
    signo =  ' Buey '
elif (año -  2000 ) %  12  ==  10 :
    signo =  ' tigre '
más :
    signo =  ' Liebre '

print ( ' Tu signo del zodiaco: ' , signo)