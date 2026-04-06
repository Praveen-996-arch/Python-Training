from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def counterclockwise():
    tim.left(30)
    # tim.circle(120)
def clockwise():
    tim.right(120)
    # tim.circle(-120)
def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

#screen class listens to the keystrokes and accordingly turtle responds
screen.listen()
screen.onkey(move_forward,"w")
screen.onkey(move_backward,"s")
screen.onkey(counterclockwise,"a")
screen.onkey(clockwise,"d")
screen.onkey(clear_drawing,"c")
screen.exitonclick()
