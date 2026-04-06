# Turtle is a module

import turtle

# Turtle class is imported from turtle module and assigned to timmy object
timmy = turtle.Turtle()
print(timmy)
# All the below are methods defined in turtle module and called by timmy object
timmy.shape("turtle")
timmy.color("blue")
timmy.forward(100)
timmy.left(120)
timmy.forward(100)
timmy.left(120)
timmy.forward(100)

my_screen = turtle.Screen()
print(my_screen.canvheight)
print(my_screen.canvwidth)

my_screen.exitonclick()