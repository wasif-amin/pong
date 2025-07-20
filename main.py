from  turtle import Turtle, Screen
from  paddles import Paddle
from  ball import Ball
from score import  Score
import  time
timmy = Turtle()
screen = Screen()


screen.setup(800, 600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)
screen.update()
timmy.color("white")
timmy.penup()
timmy.goto(0,-380)
timmy.setheading(90)
for _ in range(50):
    timmy.pendown()
    timmy.forward(8)
    timmy.penup()
    timmy.forward(8)

r_paddle = Paddle((350, 0), "blue")
l_paddle = Paddle((-350, 0), "white")
ball = Ball()
score = Score()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


game = True
while game:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.move_speed < 0:
        ball.move_speed =0.1

    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()

    if ball.distance(r_paddle) < 35 and ball.xcor() > 335 or  ball.distance(l_paddle) < 35 and ball.xcor() > -355:
        ball.bounce_x()

    if ball.xcor() > 395:
        ball.reset_position()
        score.l_point()


    if ball.xcor() < -395:
        ball.reset_position()
        score.r_point()














screen.exitonclick()
