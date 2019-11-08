# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 02:14:47 2019

@author: Jesús García
"""

##Ejercicio:  51 "Calificación de letras a puntos de calificación"

grado =  entrada ( ' ¿Cuál es el grado de letra? ' )
grade = grade.upper ()
gpa =  0

mientras  cierto :
    si grado ==  ' A + ' :
        gpa =  4.0
        rotura
    elif grade ==  ' A ' :
        gpa =  4.0
        rotura
    elif grade ==  ' A- ' :
        gpa =  3.7
        rotura
    elif grade ==  ' B + ' :
        gpa =  3.3
        rotura
    elif grade ==  ' B ' :
        gpa =  3.0
        rotura
    elif grade ==  ' B- ' :
        gpa =  2.7
        rotura
    elif grade ==  ' C + ' :
        gpa =  2.3
        rotura
    elif grade ==  ' C ' :
        gpa =  2.0
        rotura
    elif grade ==  ' C- ' :
        gpa =  1.7
        rotura
    elif grade ==  ' D + ' :
        gpa =  1.3
        rotura
    grado elif ==  ' D ' :
        gpa =  1.0
        rotura
    elif grade ==  ' F ' :
        gpa =  0
        rotura
    más :
        print ( ' Entrada inválida ' )
        grado =  entrada ( ' ¿Cuál es el grado de letra? ' )
        grade = grade.upper ()
        gpa =  0 
        
print ()
print ( ' Puntos de calificación: ' , str (gpa))