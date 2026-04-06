from turtle import Turtle,Screen

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
X_COR = [(0,0),(-20,0),(20,0)]

class Snake:
    def __init__(self):
        # self.x_cor = [0,-20,20]
        # self.y_cor = [0]
        self.move_distance = 20
        self.snake_body=[]
        self.create_snake()

    #creating a snake body by creating three instances
    def create_snake(self):
        for position in X_COR:
            self.add_segment(position)
    def add_segment(self,position):
        snake = Turtle()
        snake.shape("square")
        snake.penup()
        snake.goto(position)
        snake.color("white")
        self.snake_body.append(snake)
    def extend_body(self):
        self.add_segment(self.snake_body[-1].position())
    #Moving snake
    def move(self):

        for body in range(len(self.snake_body)-1,0,-1):
            new_x = self.snake_body[body - 1].xcor()
            new_y = self.snake_body[body - 1].ycor()
            self.snake_body[body].goto(new_x,new_y)

        self.snake_body[0].forward(self.move_distance)

    def up(self):
        if self.snake_body[0].heading() != DOWN:
            self.snake_body[0].setheading(UP)
    def down(self):
        if self.snake_body[0].heading() != UP:
            self.snake_body[0].setheading(DOWN)

    def left(self):
        if self.snake_body[0].heading() != RIGHT:
            self.snake_body[0].setheading(LEFT)

    def right(self):
        if self.snake_body[0].heading() != LEFT:
            self.snake_body[0].setheading(RIGHT)

    def reset(self):
        for body in self.snake_body:
            body.goto(1000,1000)
        self.snake_body.clear()
        self.create_snake()