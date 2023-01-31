from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('White')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.speed_x = 0.13
        self.speed_y = 0.13
        self.goto(0, 0)

    def move(self) -> None:
        self.goto(self.xcor() + self.speed_x, self.ycor() + self.speed_y)
        if self.ycor() > 290 or self.ycor() < -280:
            self.speed_y *= -1

        # Bounce right and left walls
        # if self.xcor() > 390 or self.xcor() < -390:
        #     self.speed_x *= -1

    def reset_ball(self):
        self.goto(0, 0)
        self.speed_x = 0.13
        self.speed_y = 0.13
        self.speed_x *= -1

    def increase_speed(self):
        self.speed_x += 0.05
        self.speed_y += 0.05
