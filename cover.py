from turtle import Turtle


class Cover(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("green")
        self.penup()
        self.goto(position)
        self.shapesize(stretch_wid=2, stretch_len=5)
        self.layers = 3

    def take_damage(self):

        self.layers -= 1
        if self.layers == 2:
            self.color("yellow")
        elif self.layers == 1:
            self.color("red")
        elif self.layers <= 0:
            self.hideturtle()
            self.goto(2000, 2000)
