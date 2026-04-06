from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.move_distance = 20
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def move_up(self):
        new_y = self.ycor() + self.move_distance
        self.goto(self.xcor(),new_y)
    
    def move_down(self):
        new_y = self.ycor() - self.move_distance
        self.goto(self.xcor(), new_y)
