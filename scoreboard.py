from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 40, "normal")


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(position)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(self.score, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
