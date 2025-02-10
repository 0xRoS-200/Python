from turtle import Turtle, Screen
import random as rd


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")
print(user_bet)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

def create_turtles():
    y_cord = -100
    for _ in range(len(colors)):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[_])
        new_turtle.penup()
        new_turtle.goto(-230, y_cord)
        y_cord += 40
        turtles.append(new_turtle)

create_turtles()

if user_bet:
    race_on = True
else:
    race_on = False

while race_on:
    for turtle in turtles:
        turtle.forward(rd.randint(1, 10))

        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Congratulations! The {winning_color} turtle won!")
            else:
                print(f"Sorry, the {winning_color} turtle won. Better luck next time!")
            break

screen.exitonclick()