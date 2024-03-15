# A12
# Shades of Blue

import turtle
turtle.colormode(255)
azul = turtle.Turtle()

azul.shape("turtle")
azul.backward(200)

for i in range(0,255,10):
    azul.forward(10)
    azul.pensize(i)
    azul.color(0,0,i)