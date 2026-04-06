from turtle import Screen
import time
from Food import Food
from Snake import Snake
from scoreboard import Scoreboard

class Snakegame:

    screen = Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor("black")
    screen.title("My Snack Game")
    screen.tracer(0)

    snake = Snake()
    screen.listen()
    screen.onkey(snake.up,"Up")
    screen.onkey(snake.down,"Down")
    screen.onkey(snake.left,"Left")
    screen.onkey(snake.right,"Right")

    food = Food()
    score = Scoreboard()
    score.update_scoreboard()

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        snake.move()
    #detect collision with food
        if snake.snake_body[0].distance(food) < 15:
            food.refresh()
            snake.extend_body()
            score.increase_score()
    #detect collision with wall
        if snake.snake_body[0].xcor() > 380 or  snake.snake_body[0].xcor() < -380 or  snake.snake_body[0].ycor() > 380 or  snake.snake_body[0].ycor() < -380:
            score.reset()
            snake.reset()
    #detect collision with tail or any part of snake body
        for body in snake.snake_body[1:-1]: #slicing the first index from the list
            if snake.snake_body[0].distance(body) < 10:
                score.reset()
                snake.reset()

















    screen.exitonclick()