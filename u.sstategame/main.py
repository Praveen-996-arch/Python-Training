from turtle import Turtle, Screen
import turtle
import pandas as pd


tim = Turtle()
screen = Screen()
screen.setup(width=900, height=900)
screen.title("U.S. States Game")
image = "/Users/manasapola/PycharmProjects/Basicsofpython/u.sstategame/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pd.read_csv("/Users/manasapola/PycharmProjects/Basicsofpython/u.sstategame/50_states.csv") 
game_is_on = True
guessed_states = []
while game_is_on:
    user_input = screen.textinput(f"{len(guessed_states)}/50 states correct", "Please enter the name of a US state:").title()
    
    for state in data.state:
        
        if user_input == state:
            guessed_states.append(state)
            tim.penup()
            x = data[data.state == state].x.iloc[0]
            y = data[data.state == state].y.iloc[0]
            tim.goto(x, y)
            tim.pencolor("black")
            tim.write(state)
        if len(guessed_states) == 50:
            game_is_on = False
            tim.write("Game Over", align="center", font=("Arial", 24, "normal"))
        if user_input == "Exit":
            game_is_on = False
           
            missing_states = [state for state in data.state if state not in guessed_states]
            missing_state_data = pd.DataFrame({"state":missing_states})
            missing_state_data.to_csv("/Users/manasapola/PycharmProjects/Basicsofpython/u.sstategame/missing_state_data.csv")

         
            


screen.exitonclick()