from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
scoreboard = Scoreboard()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
game_is_on = True


def end_game():
    global game_is_on
    scoreboard.goto(0, -40)
    scoreboard.write("You Quit", align="center", font=("courier", 50, "normal"))
    game_is_on = False


screen.listen()
screen.onkeypress(key="Up", fun=r_paddle.move_up)
screen.onkeypress(key="Down", fun=r_paddle.move_down)
screen.onkeypress(key="w", fun=l_paddle.move_up)
screen.onkeypress(key="s", fun=l_paddle.move_down)

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with the r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect r_paddle miss
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()

    # detect l_paddle miss
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()

    if screen.onkeypress(key="g", fun=end_game):
        # game_is_on = False
        pass

screen.exitonclick()
