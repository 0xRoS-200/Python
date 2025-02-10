from turtle import Screen, Turtle

class Display:
    def __init__(self):
        self.screen = Screen()
        self.divider = Turtle()

    def make_screen(self):
        self.screen.title("Pong")
        self.screen.bgcolor("black")
        self.screen.setup(width=800, height=600)
        self.screen.tracer(0)

    def exit_screen(self):
        self.screen.exitonclick()

    def draw_divider(self):
        self.divider.hideturtle()
        self.divider.penup()
        self.divider.setposition(0,300 )
        self.divider.setheading(270)
        self.divider.pendown()
        self.divider.color("white")
        self.divider.pensize(5)
        for i in range(30):
            self.divider.forward(10)
            self.divider.pencolor("black")
            self.divider.forward(10)
            self.divider.pencolor("white")
        self.divider.hideturtle()
        self.make_screen()
