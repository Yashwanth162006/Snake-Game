from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.color("blue")
        x = random.randrange(-350, 350)
        y = random.randrange(-250, 250)
        self.goto(x,y)

    def move(self):
        x = random.randrange(-350, 350)
        y = random.randrange(-250, 250)
        self.goto(x, y)