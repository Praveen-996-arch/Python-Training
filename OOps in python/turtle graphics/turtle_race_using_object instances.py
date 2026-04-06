#Build a turtle race
import turtle
from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=800,height=600)


user_bet = screen.textinput(title = "Guess the winner", prompt= "Enter the turtle color who you are expecting to be the winner")
colors = ["red","orange","yellow","green","blue","violet","purple"]
y_position = [240,160,70,-30,-130,-200]
all_turtles = []
for i in range(0,6):
    tim = Turtle()
    tim.shape("turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(-380,y_position[i])
    all_turtles.append(tim)

is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 380:
            is_race_on = False
            winning_color = turtle.pencolor()
            if turtle.color == user_bet:
                print(f"You Win!. The winning color is {winning_color}")
            else:
                print(f"You Lose!. The winning color was {winning_color}")
        turtle.forward(random.randint(1, 50))

screen.exitonclick()
