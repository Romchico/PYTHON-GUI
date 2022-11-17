from turtle import Turtle

ALINGMENT = "CENTER"
FONT = ("Courier", 15, "normal" )

class Scoreboard(Turtle):


    def __init__(self):
        super(Scoreboard, self).__init__()
        self.level = 0
        self.create_scoreboard()

    def create_scoreboard(self):
        self.clear()
        self.penup()
        self.hideturtle()
        self.goto(-250, 275)
        self.color("black")
        self.write(arg=f"Level: {self.level}", align=ALINGMENT, font=FONT)


    def increase_score(self):
        self.level += 1
        self.create_scoreboard()


    def game_over(self):
        self.clear()
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.color("black")
        self.write(arg="GAME OVER!", align=ALINGMENT, font=FONT)