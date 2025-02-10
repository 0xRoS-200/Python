from turtle import Turtle
import random as rd
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def car_create(self):
        random_chance = rd.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(rd.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.setheading(180)
            new_car.goto(300, rd.choice(range(-250, 250, 20)))
            self.all_cars.append(new_car)

    def car_move(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT


