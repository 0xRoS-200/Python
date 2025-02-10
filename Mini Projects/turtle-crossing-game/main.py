import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

mandy_the_turtle = Player()
cars = CarManager()
scoreboard = Scoreboard()

#setting up controls
screen.listen()
screen.onkey(mandy_the_turtle.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    #create and move cars
    cars.car_create()
    cars.car_move()

    #detect collision
    for car in cars.all_cars:
        if car.distance(mandy_the_turtle) < 30:
            scoreboard.game_over()
            game_is_on = False

    #player reaching other side
    if mandy_the_turtle.is_at_finish_line():
        mandy_the_turtle.reset_position()
        cars.increase_speed()
        scoreboard.update_score()



screen.exitonclick()