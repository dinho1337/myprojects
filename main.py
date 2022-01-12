from turtle import Turtle, Screen
import random


def draw_line():
    for _ in range(10):
        color = random.choice(color_list)
        turtle.pencolor(color)
        turtle.dot(20)
        turtle.penup()
        turtle.forward(50)


def set_next_line():
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(500)
    turtle.right(180)


#create objects
turtle = Turtle()
screen = Screen()

#color list from image.jpg
color_list = [(227, 232, 236), (55, 107, 149), (144, 91, 57), (225, 134, 57), (196, 144, 171), (234, 200, 99), (140, 180, 207), (231, 224, 192), (219, 94, 58), (130, 183, 131), (141, 100, 129), (187, 77, 127), (65, 155, 87), (51, 155, 196), (228, 234, 233), (130, 133, 74), (225, 211, 218), (56, 140, 101), (216, 176, 191), (21, 68, 112), (17, 61, 104), (223, 177, 168), (113, 123, 151), (185, 189, 205), (174, 202, 183), (171, 200, 207), (80, 58, 40), (84, 63, 41), (176, 34, 24)]
screen.colormode(255)

#speed for quickness
turtle.speed("fastest")

#for looks
turtle.hideturtle()

#set turtle in bottom left-ish
turtle.setheading(225)
turtle.penup()
turtle.forward(320)
turtle.setheading(0)

#draw
for _ in range(10):
    draw_line()
    set_next_line()

screen.exitonclick()
