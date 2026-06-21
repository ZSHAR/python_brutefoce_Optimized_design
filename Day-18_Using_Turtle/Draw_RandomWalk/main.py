from turtle import Turtle,Screen,colormode
from random_walk import RandomWalk
sam=Turtle()
sam.shape("turtle")
colormode(255)
sam.width(10)
sam.speed("fastest")
directions=[0,90,180,270]
r1=RandomWalk()
r1.random_walk(sam,100)
screen = Screen()
screen.exitonclick()