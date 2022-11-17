from turtle import Turtle
import random

COLORS = ["red", "blue", "black", "pink", "green", "purple", "orange", "yellow"]
POSITIONS_X = list(range(320,360)) # I am creating cars out of sight, then they come within the sight.
POSITIONS_Y = list(range(-250, 251, 30))
class Cars():


    def __init__(self):
        self.cars = []
        self.create_cars()
        self.speed = 0.5


    def create_cars(self):

        for _ in range(0, random.randrange(3, 4, 1)):
            pos_x = random.choice(POSITIONS_X)
            pos_y = random.choice(POSITIONS_Y)
            car_is_suitable = True
            for old_car in self.cars:  # I'm checking to make sure the cars don't overlap.

                if abs(old_car.xcor() - pos_x) < 41 and old_car.ycor() == pos_y:
                    car_is_suitable = False

            if car_is_suitable == False:
                continue


            car = Turtle()
            car.penup()
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2) # Rectangular cars 20 to 40.
            car.color(random.choice(COLORS))
            car.goto(pos_x, pos_y)
            car.right(180)
            self.cars.append(car)


    def check_max_xcor(self):
        '''Checking the furthest car if it is
    inside of the sight, if it is, then create randomly new cars.'''

        temp_lst = []

        for car in self.cars:
            temp_lst.append(car.xcor())

        ind = temp_lst.index(max(temp_lst))
        if self.cars[ind].xcor() < 280:
            self.create_cars()


    def move_cars(self):
        self.check_max_xcor()
        for car in self.cars:
            if car.xcor() < -320:
                self.cars[self.cars.index(car)].hideturtle()
                self.cars.remove(car)
            car.forward(self.speed)

    def hide_cars(self): # if game is over, I hide the cars.
        for car in self.cars:
            car.hideturtle()




