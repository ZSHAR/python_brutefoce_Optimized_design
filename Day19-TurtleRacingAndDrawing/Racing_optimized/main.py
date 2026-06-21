from turtle import Turtle, Screen
import random
from race_brain import Start_race
colors=["red","yellow","green","blue","purple","indigo","violet","orange"]
backward=[50,100,0,-50,-100,-150,150]
screen=Screen()
screen.setup(width=500, height=400)
is_race_on=False
user_bet=screen.textinput(title="Make your bet",prompt="which turtle will win the race")
turtle_list=[]
for i in range(7):
    new_turtle=Turtle("turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-240, backward[i])
    turtle_list.append(new_turtle)
if user_bet:
    is_race_on=True
while is_race_on:
    for turtle in turtle_list:
        rand_distance=random.randint(0,10)
        if turtle.xcor()>230:
            winning_color=turtle.pencolor()
            is_race_on=False
        turtle.forward(rand_distance)

if winning_color.lower()==user_bet.lower():
    print("You win!")
else:
    print("You lose!")
    print(f"this {winning_color} turtle has won")
#sher=Turtle("turtle")
#sher.color(random.choice(colors))
#sher.penup()
#sher.goto(-240,180)
