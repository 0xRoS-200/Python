import turtle
import time
import math

# Setup the turtle screen
screen = turtle.Screen()
screen.setup(800, 400)
screen.bgcolor("black")
screen.title("Dynamic Digital Clock")
screen.tracer(0)  # Turn off animation for smoother updates
screen.colormode(255)  # Use RGB values up to 255

# Create and setup the time turtle
clock = turtle.Turtle()
clock.hideturtle()
clock.penup()


def update_clock():
    clock.clear()

    # Dynamic color based on current second
    current_second = int(time.strftime("%S"))
    # Cycle through a gradient of colors using sine function for smooth transition
    r = int(127.5 * (1 + math.sin(current_second * 0.1)))
    g = int(127.5 * (1 + math.sin(current_second * 0.1 + 2)))
    b = int(127.5 * (1 + math.sin(current_second * 0.1 + 4)))

    dynamic_color = (r, g, b)

    # Shadow effect
    clock.color("black")
    clock.goto(-5, -5)
    clock.write(time.strftime("%H:%M:%S"), align="center", font=("Arial", 60, "bold"))

    # Actual time with dynamic color
    clock.color(dynamic_color)
    clock.goto(0, 0)
    clock.write(time.strftime("%H:%M:%S"), align="center", font=("Arial", 60, "bold"))

    screen.update()
    screen.ontimer(update_clock, 1000)


update_clock()

# Keep the window open
screen.mainloop()
