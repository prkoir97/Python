# A30
# Turtle String

import turtle

# Create a turtle named 'daisy'
daisy = turtle.Turtle()

# Create a screen to display turtle graphics
myWin = turtle.Screen()

commands = input("Please enter a command string: ")

# Iterate over each character in the command string
for ch in commands:         # Execute different actions based on the command character
    if ch == 'F':
        daisy.forward(50)
    elif ch == 'L':
        daisy.left(90)
    elif ch == 'R':
        daisy.right(90)
    elif ch == '^':
        daisy.penup()
    elif ch == 'v':
        daisy.pendown()
    elif ch == 'B':
        daisy.backward(50)
    elif ch == 'g':
        daisy.color("green")
    elif ch == 'b':
        daisy.color("blue")
    elif ch == 'S':
        daisy.stamp()
    elif ch == 'l':
        daisy.left(45)
    elif ch == 'r':
        daisy.right(45)
    elif ch == 'p':
        daisy.color("purple")
    else:
        # Print an error message if an unknown command is encountered
        print("Error: do not know the command:", ch)

print("See graphics window for your image")

# Wait for the user to click on the graphics window to exit
myWin.exitonclick()