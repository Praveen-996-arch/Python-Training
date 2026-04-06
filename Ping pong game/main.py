from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle
from pong_ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball=Ball()
screen.listen()
scoreboard = Scoreboard()

screen.onkey(r_paddle.move_up,"Up")
screen.onkey(r_paddle.move_down,"Down")
screen.onkey(l_paddle.move_up,"w")
screen.onkey(l_paddle.move_down,"s")


is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.refresh()

    #detect collision with wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce()

    # detect collision with paddle
    if ball.xcor() > 340 and ball.distance(r_paddle) < 50:
        ball.paddle_bounce()
       
        scoreboard.r_increase_score()
    elif ball.xcor() < -340 and ball.distance(l_paddle) < 50:
        ball.paddle_bounce()
        
        scoreboard.l_increase_score()

    #when paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_increase_score()

    elif ball.xcor() < -380:        
        ball.reset_position()
        scoreboard.r_increase_score()
        
   












screen.exitonclick()