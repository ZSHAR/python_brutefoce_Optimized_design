import turtle
from random import randint

class Shape:
    def pick_color(self):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return r, g, b

    def draw_shape(self, turtle,length,sides):
        turtle.color(self.pick_color())
        for i in range(sides):
            turtle.forward(length)
            turtle.left(360/sides)
    def draw_dash(self, turtle,line):
        for i in range(line):
            turtle.down()
            turtle.forward(10)
            turtle.up()
            turtle.forward(10)
    def draw_spirograph(self,turtle,radius,times):
        for i in range(times):
            turtle.color(self.pick_color())
            turtle.circle(radius)
            turtle.setheading(turtle.heading()+5)