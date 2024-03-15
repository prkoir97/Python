# A41
# Turtle Triangles

import turtle

# Function to set up the turtle's initial position and color
def setUp(t, dist, col):
    t.penup()
    t.forward(dist)
    t.pendown()
    t.color(col)

# Function to draw a triangle recursively
def triangle(t, length):
    if length > 10:
        for i in range(3):
            t.forward(length)
            t.left(120)
        triangle(t, length / 2)  # Call the function recursively with half the length

# Function to draw nested triangles recursively
def nestedTriangle(t, length):
    if length > 10:
        for i in range(3):
            t.forward(length)
            t.left(120)
            nestedTriangle(t, length / 2)  # Call the function recursively with half the length

# Main function
def main():
    # Prompt the user to enter the length of the largest triangle
    n = int(input('Enter length: '))

    # Create two turtle objects
    tom = turtle.Turtle()
    tess = turtle.Turtle()

    # Set up the initial positions and colors for the turtles
    setUp(tom, -100, "darkgreen")
    setUp(tess, 100, "steelblue")

    # Draw the larger triangle with tom
    triangle(tom, n)

    # Draw the nested triangles with tess
    nestedTriangle(tess, n)

# Entry point of the program
if __name__ == "__main__":
    main()
