from turtle import Turtle
import winsound


class Scoreboard(Turtle):
    def __init__(self, lives=3):
        super().__init__()
        self.lives = lives
        self.score = 0
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, -350)
        self.draw_line()
        self.update_scoreboard()

    def draw_line(self):
        self.goto(-600, -300)
        self.pendown()
        self.forward(1200)
        self.penup()
        self.goto(0, -350)

    def update_scoreboard(self):
        self.clear()
        self.goto(-520, -360)
        self.write(f"Lives: {self.lives}", align="left", font=("Arial", 19, "normal"))
        self.goto(480, -360)
        self.write(f"Score: {self.score}", align="right", font=("Arial", 19, "normal"))
        self.goto(0, -360)
        self.write(f"Level: {self.level}", align="center", font=("Arial", 19, "normal"))
        self.draw_line()

    def increase_score(self, points):
        self.score += points
        self.update_scoreboard()

    def decrease_life(self):
        self.lives -= 1
        self.update_scoreboard()
        self.play_sound()

    def play_sound(self):
        winsound.Beep(500, 200)

    def game_over(self):
        self.color("red")
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 24, "bold"))

    def reset(self):
        self.lives = 3
        self.score = 0
        self.level = 1
        self.update_scoreboard()

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()
        self.goto(0, 0)
        self.write(f"Level {self.level}", align="center", font=("Arial", 24, "bold"))
