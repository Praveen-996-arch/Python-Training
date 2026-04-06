from turtle import Turtle,Screen

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-250, 270)
        self.write(f"Level:{self.score}" ,False,'center',('Arial', 15,'normal'))
        
    def update_score(self):
      
        self.score += 1
        self.clear()
        self.write(f"Level:{self.score}" ,False,'center',('Arial', 15,'normal'))

    def game_over(self):
       
        self.goto(0,0)
        self.write("Game Over", align="center", font=("Arial", 24, "normal"))

    