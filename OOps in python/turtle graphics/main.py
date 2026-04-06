import random
from turtle import Turtle, Screen, begin_fill, end_fill

tim = Turtle()
tim.shape("arrow")
tim.resizemode("user")
tim.shapesize(0.5,0.5,0.5)
tim.color("red")

# Drawing multiple shapes from same point one after the other
colors = ["red", "blue", "green", "orange", "purple", "cyan","pale goldenrod","light steel blue"]
i = 3
j=0
while i <=10:
    tim.pencolor(random.choice(colors))
    for n in range(i):
        tim.forward(100)
        tim.right(360/i)
    i+=1
    # j+=1

# #Draw Dashed line
# for i in range(10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()








screen = Screen()
screen.exitonclick()