from turtle import  Screen
import time
from scoreboard import Scoreboard
from player import Player
from car_manager import Car

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Capstone")
screen.tracer(0)

t=Player()
screen.listen()
screen.onkey(t.move_forward,"Up")
scoreboard = Scoreboard()


car = Car()
cars_list = [car]
is_game_on = True
loop = 0
while is_game_on:
    time.sleep(0.1) 
    screen.update()
    if loop % 6 == 0:
        car = Car()
        cars_list.append(car)
    for car in cars_list:
        car.move()
    loop += 1
    # turtle collision with car
    for car in cars_list:
        if t.distance(car) < 20 and car.xcor() < 0 or car.xcor() > 0 and t.distance(car) < 20:
            is_game_on = False
            scoreboard.game_over()
            
    # successful crossing, update the level and increase the speed of the cars
    if t.ycor() > 280:
        t.is_at_finish_line()
        car.increase_speed()
        scoreboard.update_score()  
       
        
            
        
        
       
    
        
    



screen.exitonclick()    