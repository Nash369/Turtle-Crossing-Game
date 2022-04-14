import turtle
import random
import time

starting_x = 0
starting_y = -280
DISTANCE = 10
sleep = 0.1
level = 1

#setting up the screen and turtle
screen = turtle.Screen()
screen.setup(700,600)
crossing_turtle = turtle.Turtle("turtle")

#placing the turtle at the bottom of the screen
crossing_turtle.penup()
crossing_turtle.setheading(90)
crossing_turtle.goto(starting_x,starting_y)

#controlling the turtle
def move_up():
    crossing_turtle.fd(10)
    
screen.onkey(move_up,"Up")
screen.listen()

#writing levels
screen.tracer(0)
writing_turtle = turtle.Turtle()
writing_turtle.penup()
writing_turtle.hideturtle()
writing_turtle.goto(-300,270)
writing_turtle.write(f"Level {level}", font=("Yu Gothic", 16,"normal"))
screen.tracer(1)

#creating the cars
cars_list = []
y_positions = [-243, -183, -123, -63, -3, 57, 117, 177, 237]
turtle.colormode(255)

game_on = True
while game_on:
    screen.tracer(0)
    car_turtle = turtle.Turtle("square")
    car_turtle.penup()
    car_turtle.shapesize(stretch_wid=1,stretch_len=2)
    car_turtle.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    car_turtle.setheading(180)
    car_turtle.goto(380,random.choice(y_positions))
    cars_list.append(car_turtle)

    for car in cars_list:
        car.forward(DISTANCE)
        if car.distance(crossing_turtle)<20:
            game_on = False
    if crossing_turtle.ycor()>= 300:
        crossing_turtle.goto(starting_x,starting_y)
        level += 1
        sleep *= 0.5
        writing_turtle.undo()
        writing_turtle.write(f"Level {level}", font=("Yu Gothic", 16,"normal"))
    screen.tracer(1)
    time.sleep(sleep)

