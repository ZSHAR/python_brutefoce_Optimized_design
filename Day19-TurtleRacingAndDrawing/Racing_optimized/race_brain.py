colors=["red","yellow","green","blue","purple","indigo","violet","orange"]
backward=[50,100,0,-50,-100,-180,180]
import random
class Start_race:
    def __init__(self,turtle):
        self.turtle=turtle

    def positionAndColor(self):
        for i in range(6):
            self.turtle.color(colors[i])
            self.turtle.penup()
            self.turtle.goto(-240,backward[i])
