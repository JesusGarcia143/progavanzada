# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 00:07:32 2019

@author: Jesús García
"""

import turtle 
i=1
ventana=turtle.Screen()
ventana.bgcolor("white")
ventana.title("Examen")

rafael=turtle.Turtle()
rafael.shape("arrow")
rafael.color('black')
rafael.pensize(1)
rafael.speed(1)

while i<50:
    rafael.color("red")
    rafael.forward(i*160)
    rafael.left(90)
    rafael.forward(i*160)
    rafael.left(90)
    rafael.forward(i*160)
    rafael.left(90)
    rafael.forward(i*140)
    rafael.left(90)
    rafael.forward(i*140)
    rafael.left(90)
    rafael.forward(i*120)
    rafael.left(90)
    rafael.forward(i*120)
    rafael.left(90)
    rafael.forward(i*100)
    rafael.left(90)
    rafael.forward(i*100)
    rafael.left(90)
    rafael.forward(i*80)
    rafael.left(90)
    rafael.forward(i*80)
    rafael.left(90)
    rafael.forward(i*60)
    rafael.left(90)
    rafael.forward(i*60)
    rafael.left(90)
    rafael.forward(i*40)
    rafael.left(90)
    rafael.forward(i*40)
    rafael.left(90)
    rafael.forward(i*20)
    rafael.left(90)
    rafael.forward(i*20)

    
    
    
    i=i+1
    
    rafael.penup()

   
ventana.mainloop()