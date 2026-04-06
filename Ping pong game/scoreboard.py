from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,0)
        self.r_score = 0
        self.l_score = 0
        self.l_position_score()
        self.r_position_score()

    def l_position_score(self):
        self.goto(-80,260)
        self.write(f"Score:{self.l_score}", align="center", font=("Courier", 24, "normal"))

    def r_position_score(self):
        self.goto(80,260)
        self.write(f"Score:{self.r_score}", align="center", font=("Courier", 24, "normal"))
    
    def r_increase_score(self):
        self.r_score += 1
        self.clear()
        self.r_position_score()
        self.l_position_score()

    def l_increase_score(self):
        self.l_score += 1
        self.clear()
        self.l_position_score()
        self.r_position_score()
    