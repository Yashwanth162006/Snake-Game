from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.display()

    def display(self):
        self.clear()
        self.write(f"Score: {self.score}",align="center",font=("Courier",15,"normal"))

    def increase_score(self):
        self.score += 1
        self.display()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over !", align="center",font=("Courier",15,"normal"))