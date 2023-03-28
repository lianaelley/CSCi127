#assignment2
#Write a program that draws a pentadecagon (polygon with fifteen sides). 

import turtle
t=turtle.Screen()
pentadecagon=turtle.Turtle()
for i in range(15):
    pentadecagon.forward(80)
    pentadecagon.left(360/15)
    
