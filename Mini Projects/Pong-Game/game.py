import ball
from display import Display
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#import screen
screen_build = Display()
screen = screen_build.make_screen()
screen_build.draw_divider()

#make paddle
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
#make ball
pong_ball = Ball()
#make scoreboard
scoreboard = Scoreboard()


#move paddles
screen_build.screen.listen()
screen_build.screen.onkeypress(r_paddle.move_up, "Up")
screen_build.screen.onkeypress(r_paddle.move_down, "Down")
screen_build.screen.onkeypress(l_paddle.move_up, "w")
screen_build.screen.onkeypress(l_paddle.move_down, "s")

game_on = True

while game_on:
    time.sleep(pong_ball.move_speed)
    screen_build.screen.update()
    pong_ball.move_ball()

    #Detect collision with wall
    if pong_ball.ycor() > 280 or pong_ball.ycor() < -280:
        #need to bounce
        pong_ball.bounce_y()

    # Detect collision with r_paddle
    if pong_ball.distance(r_paddle) < 50 and pong_ball.xcor() > 320 or pong_ball.distance(l_paddle) < 50 and pong_ball.xcor() < -320:
        pong_ball.bounce_x()

    #Detect right paddle misses
    if pong_ball.xcor() > 380:
        pong_ball.reset_position()
        scoreboard.l_point()

    # Detect left paddle misses
    if pong_ball.xcor() < -380:
        pong_ball.reset_position()
        scoreboard.r_point()


#delete screen
screen_build.exit_screen()