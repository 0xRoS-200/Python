from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard:
    def __init__(self):
        self.score = 0
        self.high_score = 0
        self.score_board = Turtle()
        self.score_board.hideturtle()
        self.score_board.penup()
        self.score_board.goto(0, 270)
        self.score_board.color("black")
        self.update_scoreboard()


    def update_scoreboard(self):
        self.score_board.clear()
        self.score_board.write(f"Score: {self.score}", align="center", font=FONT)

    def update_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.score_board.goto(0, 0)
        self.score_board.write("GAME OVER", align="center", font=FONT)
