from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x=350, y=0):
        super().__init__()
        self.speed(0)
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x, y)

    def go_up(self) -> None:
        if self.ycor() < 235:
            self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self) -> None:
        if self.ycor() > -235:
            self.goto(self.xcor(), self.ycor() - 20)

    def reset_left_paddle(self):
        self.goto(-350, 0)

    def reset_right_paddle(self):
        self.goto(350, 0)
