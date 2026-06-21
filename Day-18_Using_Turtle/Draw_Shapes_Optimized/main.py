
from turtle import Turtle, Screen,colormode
from draw_shape import Shape
sam=Turtle()
sam.shape("turtle")
colormode(255)
sam.speed("fastest")
s1=Shape()
#for sides in range(3,11):
    #s1.draw_shape(sam,40,sides)
s1.draw_spirograph(sam,150,80)
screen = Screen()
screen.exitonclick()