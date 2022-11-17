from turtle import Turtle

STARTING_POSITION = (0, -280)

class Player(Turtle):

    def __init__(self):
        super(Player, self).__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)

    def go_forward(self):
        self.forward(10)
