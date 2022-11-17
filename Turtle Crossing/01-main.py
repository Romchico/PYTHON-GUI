from turtle import Screen
from scoreboard import Scoreboard
from cars import Cars
from player import Player
from time import sleep

starting_position = (0, -280)

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0) # Updates are not shown in the screen


player = Player()
scoreboard = Scoreboard()
cars = Cars()

screen.listen()
screen.onkey(player.go_forward, "Up")
screen.tracer(1) # Updates are shown in the screen


def game_over():
    screen.tracer(0)
    cars.hide_cars()
    player.hideturtle()
    scoreboard.game_over() # I wanna just see GAME OVER! nothing more.
    sleep(1)
    screen.tracer(1)


def check_collision():
    '''When we calculate the distance between turtle and car, we consider the bottom of
    turtle, for car we consider the center of the rectangle! The width of car is 40,
    the height is 20. The height of turtle is 20 as well.
    '''
    for car in cars.cars:
        if -20 < car.xcor() < 20: # If the cars are not in this range, then we can continue!
            pass
        else:
            continue
        if abs(player.ycor() - car.ycor()) < 11:
            '''It means if the turtle near to the car not, i.e 
            not above or below!'''
            if player.xcor() - car.xcor() < 22.3:
                '''I did some geometry, 10~20~10sqrt(5)
                10sqrt(5) equals about 22.36'''
                game_over()
                return True
            else:
                continue

        elif player.ycor() < car.ycor() and abs(player.ycor() - car.ycor()) < 30:
            '''If turtle is blow the car, then we need to calculate according to this situation
            because as I said, we consider the bottom of the turtle when measuring the distance!'''
            game_over()
            return True


game_is_on = True
while game_is_on:
    if player.ycor() > 280: # When player reaches the top
        screen.tracer(0)
        player.goto(starting_position)
        scoreboard.increase_score()
        cars.speed += 0.1
        screen.tracer(1)
    screen.tracer(0)
    cars.move_cars()
    if check_collision() == True:
        break
    screen.tracer(1)


screen.exitonclick()
