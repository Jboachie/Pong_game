from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,coord):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.goto(coord)
        self.shapesize(stretch_len=5)
        self.setheading(90)

    def moveup(self):
        self.forward(20)

    def movedown(self):
        self.back(20)
