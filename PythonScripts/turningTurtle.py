# A18
# Turning Turtle

n1 = input('Enter a number: ')
n2 = input('Enter a number: ')
n3 = input('Enter a number: ')
n4 = input('Enter a number: ')
n5 = input('Enter a number: ')

import turtle
stripe = turtle.Turtle()

for i in range(1):
    stripe.forward(100)
    stripe.left(int(n1))
    stripe.forward(100)
    stripe.left(int(n2))
    stripe.forward(100)
    stripe.left(int(n3))
    stripe.forward(100)
    stripe.left(int(n4))
    stripe.forward(100)
    stripe.left(int(n5))
