from turtle import Turtle


class Alien(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=0.75)
        self.penup()
        self.goto(position)
