from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 20, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 370)
        self.highscore = 0
        with open("Snakegame/High_score.txt") as file:
            self.highscore = int(file.read())
        # self.write(f"Score:{self.score}" ,False,'center',('Arial', 15,'normal'))
        # self.increase_score()
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score}   High Score: {self.highscore}", False, ALIGNMENT, FONT)

    def reset(self):   
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_scoreboard()
        with open("Snakegame/High_score.txt", mode="w") as file:
            file.write(f"{self.highscore}")
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
    
    

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over",False, 'center', ('Arial', 20, 'normal'))

