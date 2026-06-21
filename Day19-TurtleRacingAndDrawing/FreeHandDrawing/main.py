from turtle import Turtle, Screen
from turtle_drawing_freeHand import DrawingFreeHand
sam=Turtle()
screen=Screen()
draw=DrawingFreeHand(sam)
screen.listen()
screen.onkey(draw.moveForward,key="w")
screen.onkey(draw.moveBackward,key="s")
screen.onkey(draw.clockwise,key="a")
screen.onkey(draw.anticlockwise,key="d")
screen.onkey(draw.clear,key="c")
screen.exitonclick()