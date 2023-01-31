from turtle import Turtle


class ScoreBoard(Turtle):
    score_left: int = 0

    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 180)
        self.print_score()

    def increase_score_right(self):
        self.clear()
        self.score_right += 1
        self.print_score()

    def increase_score_left(self):
        self.clear()
        self.score_left += 1
        self.print_score()

    def print_score(self):
        self.write(f'{self.score_left}    {self.score_right}', move=False, align='center',
                   font=('Courier', 80, 'normal'))
