from turtle import Turtle


class Bullet(Turtle):
    def __init__(self, position, direction):
        super().__init__()
        self.shape("square")
        self.color("green" if direction == 1 else "red")
        self.shapesize(stretch_wid=1, stretch_len=0.15)
        self.penup()
        self.goto(position)
        self.moving = True
        self.direction = direction

    def move(self, speed=1):
        if self.moving:
            self.sety(self.ycor() + self.direction * speed)
            if self.ycor() > 600 or self.ycor() < -290:
                self.moving = False
                return False
        return True

    def check_collision(self, target):
        if self.distance(target) < 25:
            self.moving = False
            return True
        return False
