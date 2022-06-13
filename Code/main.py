import random
from turtle import *

tim = Turtle()
colormode(255)


def colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


tim.hideturtle()
tim.speed("fastest")
tim.penup()
tim.setheading(225)
tim.forward(250)
tim.setheading(0)
number_of_dots = 100


for dot_number in range(1, number_of_dots + 1):
    tim.dot(20, colour())
    tim.penup()
    tim.forward(50)

    if dot_number % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = Screen()
screen.exitonclick()
