import turtle
from turtle import Turtle
import random

tim = Turtle()

turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

for i in range(20):
    current_heading = tim.heading()
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(current_heading + 10)
