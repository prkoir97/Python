# A47
# Random Walk

import turtle
import random

# Create a turtle named trey
trey = turtle.Turtle()

# Set the drawing speed to 10 (maximum speed)
trey.speed(10)

# Iterate 100 times to draw 100 lines
for i in range(100):
  # Move the turtle forward by 30 units
  trey.forward(30)

  # Generate a random angle between 0 and 360 in increments of 10
  a = random.randrange(0, 360, 10)

  # Turn the turtle to the right by the randomly generated angle
  trey.right(a)
