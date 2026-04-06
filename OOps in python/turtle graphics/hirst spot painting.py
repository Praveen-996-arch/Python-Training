import turtle

import colorgram
from turtle import Turtle
import random
 #Extracting colors from the image
# colors = colorgram.extract('image.jpg', 20)
# i=0
# image_tuple = []
# #exrtacting rgb colors from the image
# for i in range(20):
#     first_color = colors[i]
#     rgb_color = first_color.rgb
#     r=rgb_color[0]
#     g=rgb_color[1]
#     b=rgb_color[2]
#     new_color = (r,g,b)
#     image_tuple.append(new_color)
#
# print(image_tuple)

tim = Turtle()
turtle.colormode(255)
tim.penup()
tim.setheading(255)
tim.forward(300)
tim.setheading(0)
j=1
color_list = [(251, 249, 245), (209, 165, 124), (249, 234, 236), (140, 49, 106), (164, 169, 38), (244, 80, 56), (228, 115, 163), (3, 143, 56), (215, 234, 231), (241, 65, 140), (50, 203, 226), (254, 230, 0), (210, 231, 234), (171, 186, 177), (27, 197, 220), (232, 165, 190)]
for j in range(10):
    for i in range(10):
        tim.dot(15, random.choice(color_list))
        tim.forward(30)
    tim.setheading(90)
    tim.forward(30)
    tim.setheading(180)
    tim.forward(300)
    tim.setheading(0)







# hsl_color = first_color.hsl
# print(hsl_color)
# proportion  = first_color.proportion
# print(proportion)
# red = rgb_color[0]
# print(red)
# green = rgb_color[1]
# print(green)
# blue = rgb_color[2]
# print(blue)