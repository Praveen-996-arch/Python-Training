import random
import turtle
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("arrow")
tim.pensize(15)
tim.speed("normal")
screen = Screen()
turtle.colormode(255)
# colors = ["red", "blue", "green", "orange", "purple", "cyan","pale goldenrod","light steel blue"]
directions = [0,90,180,270]

def random_color():
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        color = (r,g,b)
        return color
for i in range(100):
        tim.color(random_color())
        tim.forward(30)
        tim.setheading(random.choice(directions))









screen = Screen()
screen.exitonclick()