from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super(Paddle, self).__init__()
        self.shape("square")
        self.color("white")
        self.pu()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.seth(90)
        self.setpos(position)

    def move_up(self):
        self.fd(10)

    def move_down(self):
        self.bk(10)
