from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

# We create an instance of the Screen class
screen = Screen()

# We create two instances of the Table class
# one for the right table and one for the left table
right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)

# We create an instance of the ball
ball = Ball()

# We create an instance of the scoreboard
scoreboard = ScoreBoard()


def main() -> None:
    # We call this two functions to set the window properties
    window_properties()
    draw_middle_line()

    # Then we set the key bindings for the right table
    screen.listen()
    screen.onkey(right_paddle.go_up, "Up")
    screen.onkey(right_paddle.go_down, "Down")
    screen.onkey(left_paddle.go_up, "w")
    screen.onkey(left_paddle.go_down, "s")

    game_is_on = True
    while game_is_on:
        screen.update()
        ball.move()
        if ball.xcor() > 330 and ball.distance(right_paddle) < 50:
            ball.speed_x *= -1
            ball.increase_speed()
        elif ball.xcor() < -330 and ball.distance(left_paddle) < 50:
            ball.speed_x *= -1
            ball.increase_speed()

        if ball.xcor() > 400:
            scoreboard.increase_score_left()
            reset()
        elif ball.xcor() < -400:
            scoreboard.increase_score_right()
            reset()

    screen.exitonclick()


def window_properties() -> None:
    screen.tracer(0)
    screen.bgcolor("black")
    screen.title("Pong")
    screen.setup(width=800, height=600)


def draw_middle_line() -> None:
    tmp_turtle = Turtle()
    tmp_turtle.hideturtle()
    tmp_turtle.speed(0)
    tmp_turtle.color('white')
    tmp_turtle.penup()
    tmp_turtle.goto(0, 300)
    tmp_turtle.setheading(270)
    for i in range(20):
        tmp_turtle.pendown()
        tmp_turtle.forward(15)
        tmp_turtle.penup()
        tmp_turtle.forward(15)


def reset():
    left_paddle.reset_left_paddle()
    right_paddle.reset_right_paddle()
    ball.reset_ball()


if __name__ == "__main__":
    main()
