from turtle import Turtle,Screen        
import random

COLORS = ["red", "blue", "yellow", "purple", "orange", "black"]
MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.cars()

    def cars(self):
        self.shape("square")
        self.color(random.choice(COLORS))
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.speed("slowest")
        self.goto(290,random.randint(-250,250))
            
    def move(self):
        self.backward(MOVE_DISTANCE)
    
    def increase_speed(self):
        global MOVE_DISTANCE
        MOVE_DISTANCE += MOVE_INCREMENT
        
        