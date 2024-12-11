from turtle import Turtle


class Spaceship(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.setheading(90)
        self.penup()
        self.goto(0, -250)
        self.shapesize(stretch_wid=2, stretch_len=2)

    def move_left(self):
        x = self.xcor()
        if x > -580:
            self.setx(x - 10)

    def move_right(self):
        x = self.xcor()
        if x < 580:
            self.setx(x + 10)
