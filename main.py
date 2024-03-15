from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

game_speed = 0.1
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

rpaddle = Paddle((350,0))
lpaddle = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()
ball.moveball()


screen.listen()
screen.onkey(rpaddle.moveup, "Up")
screen.onkey(rpaddle.movedown, "Down")
screen.onkey(lpaddle.moveup, "w")
screen.onkey(lpaddle.movedown, "s")

game_is_on = True
while game_is_on:
    time.sleep(game_speed)
    screen.update()
    ball.moveball()
#Detect collision with wall and rebound
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
#Detect collision with paddle
    if ball.distance(rpaddle) < 50 and ball.xcor() > 320 or ball.distance(lpaddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        game_speed *= 0.9
#Detect right paddle miss and restart
    if ball.xcor() > 400:
        ball.restart()
        scoreboard.lpoint()
        ball.moveball()
        game_speed = 0.1

#Detect left paddle miss and restart
    if ball.xcor() < -400:
        ball.restart()
        scoreboard.rpoint()
        ball.moveball()
        game_speed = 0.1

























screen.exitonclick()