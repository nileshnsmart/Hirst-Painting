###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##

from turtle import Turtle
from turtle import Screen
import turtle
import random
tim = Turtle()
turtle.colormode(255)
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
k = 0
y = -200
tim.up()
tim.hideturtle()
for i in range(10):
    tim.setpos(-200,y)
    for j in range(10):
        tim.dot(20, color_list[k])
        tim.forward(50)
        k = random.randint(0,len(color_list)-1)
    y = y + 50


screen = Screen()
screen.exitonclick()
